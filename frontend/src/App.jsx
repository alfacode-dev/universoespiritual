import React, {useState} from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

export default function App(){
  const [username, setUsername] = useState('')
  const [fullname, setFullname] = useState('')
  const [token, setToken] = useState('')
  const [userResult, setUserResult] = useState('')

  const [itemName, setItemName] = useState('')
  const [itemDesc, setItemDesc] = useState('')
  const [items, setItems] = useState([])

  async function createUser(){
    const res = await fetch(`${API_BASE}/users`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({username, full_name: fullname})
    })
    const txt = await res.text()
    setUserResult(res.status + '\n' + txt)
  }

  async function createItem(){
    const headers = {'Content-Type':'application/json'}
    if(token) headers['Authorization'] = `Bearer ${token}`
    const res = await fetch(`${API_BASE}/items`, {
      method: 'POST', headers, body: JSON.stringify({name: itemName, description: itemDesc})
    })
    const txt = await res.text()
    await fetchItems()
    setUserResult(txt)
  }

  async function fetchItems(){
    const res = await fetch(`${API_BASE}/items`)
    const data = await res.json()
    setItems(data)
  }

  return (
    <div className="container">
      <h1>UniversoEspiritual — Preview (React)</h1>
      <div className="row">
        <label>Token: <input value={token} onChange={e=>setToken(e.target.value)} placeholder="optional token"/></label>
      </div>

      <section>
        <h2>Create user</h2>
        <input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} />
        <input placeholder="full name" value={fullname} onChange={e=>setFullname(e.target.value)} />
        <button onClick={createUser}>Create</button>
        <pre>{userResult}</pre>
      </section>

      <section>
        <h2>Create item</h2>
        <input placeholder="name" value={itemName} onChange={e=>setItemName(e.target.value)} />
        <input placeholder="description" value={itemDesc} onChange={e=>setItemDesc(e.target.value)} />
        <button onClick={createItem}>Create Item</button>
      </section>

      <section>
        <h2>Items</h2>
        <button onClick={fetchItems}>Refresh</button>
        <div>
          {items.map(it=> <div key={it.id} className="item">{JSON.stringify(it)}</div>)}
        </div>
      </section>
    </div>
  )
}
