import React from 'react';
import { useDispatch } from 'react-redux';
import {gradeQuestion} from './resultSlice.js';

export default function Question(props) {
    const dispatch = useDispatch();
    const id = props.def.id;
    const question = props.def.question;
    const choices = props.def.choices;
    return (
        <div className="question ml-sm-5 pl-sm-5 pt-2">
            <div className="py-2 h5"><b>{question}</b></div>
            <div className="ml-md-3 ml-sm-3 pl-md-5 pt-sm-0 pt-3" id="options">
                {choices.map((choice) => (
                    <label className="options" data-testid={"q" + id + "choice" + choice.id}>{choice.text}
                        <input type="radio" name={"radio" + id} onClick={() => dispatch(gradeQuestion([Number(id), Boolean(choice.correct)]))}/>
                        <span className="checkmark"></span>
                    </label>
                ))}
            </div>
        </div>
    );
}
// export default class Question extends React.Component {
    
//     constructor(props) {
//         super(props);
//         this.state = {
//             id: props.def.id,
//             question: props.def.question,
//             choices: props.def.choices,
//             grader: props.grader
//         };
//     }
//     render() {
//         return (
//             <div className="question ml-sm-5 pl-sm-5 pt-2">
//                 <div className="py-2 h5"><b>{this.state.question}</b></div>
//                 <div className="ml-md-3 ml-sm-3 pl-md-5 pt-sm-0 pt-3" id="options">
//                     {this.state.choices.map((choice) => (
//                         <label className="options" data-testid={"q" + this.state.id + "choice" + choice.id}>{choice.text}
//                             <input type="radio" name={"radio" + this.state.id} onClick={() => this.state.grader(this.state.id, choice.correct)}/>
//                             <span className="checkmark"></span>
//                         </label>
//                     ))}
//                 </div>
//             </div>
//         );
//     }
// }