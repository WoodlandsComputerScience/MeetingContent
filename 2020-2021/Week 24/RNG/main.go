package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/CrowdSurge/banner"
	"github.com/olekukonko/tablewriter"
)

type Data []P

type P struct {
	Name    string
	Entries int
}

func (d *Data) size() int {
	return len(*d)
}

var DATA = Data{
	{
		Name:    "Sachan",
		Entries: 1,
	},
	{
		Name:    "Sujash",
		Entries: 1,
	},
	{
		Name:    "Leon",
		Entries: 2,
	},
	{
		Name:    "Kaushik",
		Entries: 3,
	},
}

func main() {
	var lottery = make([]string, 0) // list of all entries
	// load data
	table := tablewriter.NewWriter(os.Stdout)
	table.SetAlignment(tablewriter.ALIGN_LEFT)
	table.SetHeader([]string{
		"Name", "Entries",
	})
	for _, p := range DATA {
		table.Append([]string{ // add to table
			p.Name,
			strconv.Itoa(p.Entries),
		})
		for i := 0; i < p.Entries; i++ { // give each person the number of entries they have
			lottery = append(lottery, p.Name)
		}
	}
	s := make([]string, len(lottery))
	copy(s, lottery)
	table.Render()

	max := DATA.size()               // number of total entries
	rand.Seed(time.Now().UnixNano()) // set seed
	rand.Shuffle(len(s), func(i, j int) { s[i], s[j] = s[j], s[i] })
	n := rand.Intn(max) // randomly select an entry
	fmt.Println("Lottery:\t", lottery)
	fmt.Println("Scrambled:\t", s)
	winner := s[n]                                           // determine winner
	banner.Print("the winner is " + strings.ToLower(winner)) // announce winner
}
