### Nodes
- [ ] Author
- [ ] Paper
- [ ] Year
- [ ] Conference
- [ ] Keyword

### Relationship
- [ ] Author  <-[:COLLABORATED]->  Author
- [ ] Author  -[:PUBLISHED]->  Paper
- [ ] Author  -[:PUBLISHED_IN]->  Year
- [ ] Paper  -[:PUBLISHED_IN]->  Year
- [ ] Author -[:PUBLISHED_AT]-> Conference
- [ ] Paper -[:PUBLISHED_AT]-> Conference
- [ ] Author -[:PUBLISHED_ABOUT]-> Keyword
- [ ] Paper -[:PUBLISHED_ABOUT]-> Keyword
- [ ] Conference -[:HELD_IN]-> Year
