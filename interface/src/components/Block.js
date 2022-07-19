import React, {useState} from "react";
import { Button } from 'react-bootstrap'
import Transaction from "./Transaction";
import {MILLISECONDS_PY} from "../config"

function ToogleTransactionDisplay({block}) {
    const [displayTransaction, setDisplayTransaction] = useState(false)
    const {data} = block

    const toggleDisplayTransaction = () => {
        setDisplayTransaction(!displayTransaction)
    }

    if (displayTransaction) {
        return (
            <div>
                {
                    data.map(transaction => (
                        <div key={transaction.id}>
                            <hr/>
                            <Transaction transaction={transaction} />
                        </div>
                    ))
                }
                <br/>
                <Button 
                    onClick={toggleDisplayTransaction} 
                    variant="danger" 
                    size="sm"
                >
                    Show Less
                </Button>
            </div>
        )
    }
    return (
        <div>
            <br/>
            <Button 
                onClick={toggleDisplayTransaction} 
                variant="danger" 
                size="sm"
            >
                Show More
            </Button>
        </div>
    )
}

function Block ({ block }) {
    const {timestamp, hash} = block
    const hashDisplay = `${hash.substring(0, 15)}...`
    const timestampDisplay = new Date(timestamp/MILLISECONDS_PY).toLocaleString()

    return (
        <div className="Block">
            <div>Hash: {hashDisplay}</div>
            <div>TimeStamp: {timestampDisplay}</div>
            <ToogleTransactionDisplay block={block}/>
        </div>
    )
}

export default Block;