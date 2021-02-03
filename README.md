# BreakingBad API *in GraphQL*
#### Preface
This repo has only purpose to make experiments with GraphQL by [Strawberry](https://github.com/strawberry-graphql/strawberry).
Dataset is retrieved from [BreakingBad Api](https://github.com/timbiles/Breaking-Bad--API).

### Meet me
```sh
cd breakingbad/
strawberry server breakingbad
```

### Play with me
#### Basic query
Retrieve all characters
```js
{
  characters {
    name
    nickname
    occupation
  }
}
```
All episodes with extra information on characters
```js
{
  episodes(filters: {}) {
    title
    season
    series
    characters {
      name
      nickname
    }
  }
}
```
#### Filter that query
```js
{
  deaths(filters:{}, responsible:{nickname: "Heisenberg"}) {
    death
    cause
  }
}
```
### Don't trust me, prove it
```sh
py.test tests
```