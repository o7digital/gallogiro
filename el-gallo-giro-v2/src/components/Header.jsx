import React, {useEffect, useRef, useState} from 'react';
import navigation from '../data/navigation.json';

export default function Header({es,setEs,order}) {
  const [mobileOpen,setMobileOpen]=useState(false);
  const [expanded,setExpanded]=useState(null);
  const header=useRef(null);
  const toggle=useRef(null);
  const buttons=useRef({});
  const close=()=>{setExpanded(null);setMobileOpen(false)};
  useEffect(()=>{
    const outside=e=>{if(!header.current?.contains(e.target))close()};
    const escape=e=>{
      if(e.key!=='Escape')return;
      if(expanded){buttons.current[expanded]?.focus();setExpanded(null)}
      else if(mobileOpen){setMobileOpen(false);toggle.current?.focus()}
    };
    document.addEventListener('pointerdown',outside);
    document.addEventListener('keydown',escape);
    return ()=>{document.removeEventListener('pointerdown',outside);document.removeEventListener('keydown',escape)};
  },[expanded,mobileOpen]);
  return <header className="navigation official-navigation" ref={header}>
    <button ref={toggle} className="nav-toggle" aria-label={es?'Menú de navegación':'Navigation menu'} aria-expanded={mobileOpen} aria-controls="official-main-navigation" onClick={()=>{setMobileOpen(!mobileOpen);setExpanded(null)}}><span aria-hidden="true">{mobileOpen?'×':'☰'}</span></button>
    <a href="#home" className="brand" onClick={close}><img src="/assets/logo.webp" alt="El Gallo Giro"/></a>
    <nav id="official-main-navigation" className={mobileOpen?'official-links is-open':'official-links'} aria-label={es?'Navegación principal':'Main navigation'}>
      <ul className="header-items">{navigation.items.map(item=><li className="header-item" key={item.id}>{item.children?<>
        <button ref={el=>{buttons.current[item.id]=el}} className="header-disclosure" aria-expanded={expanded===item.id} aria-controls={'header-submenu-'+item.id} onClick={()=>setExpanded(expanded===item.id?null:item.id)}>{es?item.es:item.en}<span aria-hidden="true">⌄</span></button>
        <ul id={'header-submenu-'+item.id} className={'header-submenu '+(item.id==='menu'?'restaurant-submenu':'')} hidden={expanded!==item.id}>{item.children.map(child=><li key={child.href}><a href={child.href} onClick={close}>{es&&child.es?child.es:child.label}</a></li>)}</ul>
      </>:<a href={item.href} onClick={close}>{es?item.es:item.en}</a>}</li>)}</ul>
    </nav>
    <div className="nav-actions"><button className="language" onClick={()=>setEs(!es)} aria-label={es?'Cambiar a inglés':'Switch to Spanish'}>{es?'EN':'ES'}</button><button className="btn small" onClick={()=>{close();order()}}>{es?'ORDENA AQUÍ':'ORDER NOW'} <span aria-hidden="true">↗</span></button></div>
  </header>;
}
