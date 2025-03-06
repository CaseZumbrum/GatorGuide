import React from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';

import CourseCard from '../CourseCard/CourseCard.js';
import Tooltip from "../ToolTip/ToolTip.tsx";


function Search() {
  const [items, setItems] = useState<string[]>([])
  const [courses, setCourses] = useState([])
  const [query, setQuery] = useState<string>("")
  const inputRef = useRef()

  const filteredItems = items.filter(item => {
    return item.toLowerCase().includes(query.toLowerCase())}
  )


  function onSubmit(e) {
    e.preventDefault()

    setCourses(currentCourses => {
      return [
        ...currentCourses,
        { courseName: newName, }
      ]
    })

    // const value = inputRef.current.value 
    // if (value === "") return

    // setItems(prev => {
    //   return [...prev, value]
    // })

    // inputRef.current.value = ""
  }

  return (
    <div>
      Search 
      <input value={query} onChange={e => setQuery(e.target.value)} type="search" />
      <br />
      <br />
      <form onSubmit={onSubmit}>
        NewItem: <input ref={inputRef} type="text"/>
        <button type="submit">Add</button>
      </form>
      <h3>Course Cards</h3>
      {filteredItems.map(CourseCard => (
        <div>{CourseCard}</div>
      ))}
    </div>
  );
}

export default Search;
