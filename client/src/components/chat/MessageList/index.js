import React, { useState, useEffect, useRef } from "react";
import Compose from "../Compose";
// import ToolbarButton from '../ToolbarButton';
import ConversationList from "../ConversationList/index";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Message from "../Message";
import { connect } from "react-redux";
import moment from "moment";
import "./MessageList.css";
import axios from "axios";
import Card from "@material-ui/core/Card";
import { animateScroll } from "react-scroll";
import CardHeader from "@material-ui/core/CardHeader";
import CardActions from "@material-ui/core/CardActions";
import { red } from "@material-ui/core/colors";
import Loading from "../../../loading.js";
import { Button, Paper } from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: "100%",
  },
  media: {
    height: 0,
    paddingTop: "56.25%", // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
  sectionDesktop: {
    display: "none",
    [theme.breakpoints.up("md")]: {
      display: "flex",
    },
  },
  sectionMobile: {
    display: "flex",
    [theme.breakpoints.up("md")]: {
      display: "none",
    },
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
  },
  secondaryHeading: {
    fontSize: theme.typography.pxToRem(15),
    color: theme.palette.text.secondary,
  },
  icon: {
    verticalAlign: "bottom",
    height: 20,
    width: 20,
  },
  details: {
    alignItems: "center",
  },
  column: {
    flexBasis: "33.33%",
  },
  helper: {
    borderLeft: `2px solid ${theme.palette.divider}`,
    padding: theme.spacing(1, 2),
  },
  link: {
    color: theme.palette.primary.main,
    textDecoration: "none",
    "&:hover": {
      textDecoration: "underline",
    },
  },
}));

const MessageLists = (props) => {
  const conversation = props.data.conversation;
  const MY_USER_ID = props.data.username;
  const user_images = props.data.user_image;

  const renderMessages = () => {
    let messages = [...conversation, ...message1];
    let i = 0;
    let messageCount = messages.length;
    let tempMessages = [];

    while (i < messageCount) {
      let previous = messages[i - 1];
      let current = messages[i];
      let next = messages[i + 1];
      let isMine = current.user === MY_USER_ID;
      let currentMoment = moment(current.timestamp);
      let prevBySameAuthor = false;
      let nextBySameAuthor = false;
      let startsSequence = true;
      let endsSequence = true;
      let showTimestamp = true;

      if (previous) {
        let previousMoment = moment(previous.timestamp);
        let previousDuration = moment.duration(
          currentMoment.diff(previousMoment)
        );
        prevBySameAuthor = previous.user === current.user;

        if (prevBySameAuthor && previousDuration.as("hours") < 1) {
          startsSequence = false;
        }

        if (previousDuration.as("hours") < 1) {
          showTimestamp = false;
        }
      }

      if (next) {
        let nextMoment = moment(next.timestamp);
        let nextDuration = moment.duration(nextMoment.diff(currentMoment));
        nextBySameAuthor = next.user === current.user;

        if (nextBySameAuthor && nextDuration.as("hours") < 1) {
          endsSequence = false;
        }
      }

      let image = user_images.filter((res) => {
        return res.user === current.user;
      })[0];
      props.scrollToBottom();
      tempMessages.push(
        <Message
          key={i}
          isMine={isMine}
          startsSequence={startsSequence}
          endsSequence={endsSequence}
          showTimestamp={showTimestamp}
          data={current}
          user_image={image ? image.image : undefined}
          user_id={MY_USER_ID}
        />
      );

      // Proceed to the next message.
      i += 1;
    }

    return tempMessages;
  };

  const [name, setName] = useState("");
  const [room, setRoom] = useState("");
  const [message, setMessage] = useState("");
  const [file, setFile] = useState();
  const [message1, setMessage1] = useState([]);
  const [users, setUsers] = useState("");
  

  const handleLike = () => {
    setMessage(message.concat("👍🏻"));
  };

  const handleEmogi = (data) => {
    setMessage(message.concat(data));
  };

  const sendMessage = (event) => {
    event.preventDefault();
    const input = message;
    setMessage("");
    props.handleSend(event, input);
  };
  const classes = useStyles();
  return (
        <div style={{
            width: "100%",
            height: '100%',
            flexFlow: "wrap",
            flexDirection: "row",
            backgroundColor: "transparent",
            boxShadow: "none",
          }}
        >
          <Button onClick={props.scrollToBottom} />
          <CardHeader
                  className="headerstyle"
                  id="ContainerElementID"
                  title={props.data.teamName}
                />
          
              <Card className={classes.root}>
              <Paper style={{ width: "100%", boxShadow: "none" }}>
                    
                    <Compose
                      handlechange={props.handlechange}
                      handleSubmit={props.handleSubmit}
                      title={props.title}
                      props={props}
                      uploadImageName={props.uploadImageName}
                      uploadImage={props.uploadImage}
                      message={message}
                      setMessage={setMessage}
                      setFile={setFile}
                      handleLoadingSend={props.handleLoadingSend}
                      sendMessage={sendMessage}
                      loadingSend={props.data.loadingSend}
                      handleLike={handleLike}
                      handleEmogi={handleEmogi}
                      handleClearImage={props.handleClearImage}
                      open={props.data.open}
                      handleOpenUploadFile={props.handleOpenUploadFile}
                      handleCloseUploadFile={props.handleCloseUploadFile}
                      handleImageUploadFile={props.handleImageUploadFile}
                        />
                  </Paper>
                

                <div id="ContainerElementID" className="message-list-container ">
                  {!props.loading1 && !props.loading ? (
                    <>{renderMessages()}</>
                  ) : (
                    <Loading />
                  )}
                </div>
              </Card>
        </div>
  );
};

class MessageList extends React.Component {
  state = {
    conversation: [],
    teamName: null,
    username: null,
    input: "",
    uploadImage: null,
    uploadImageName: '',
    image: null,
    user_image: [],
    showEmojiPicker: false,
    activeUsersList: [],
    isactive: false,
    loading: true,
    loadingSend: false,
    open: false
  };


  handleImageUploadFile=(data)=>{
    const image = data[0];
    console.log(image);
    this.setState({
      uploadImage : image,
      uploadImageName: image.name
    });
    this.handleCloseUploadFile();
  }

  handleClearImage=()=>{
    this.setState({
      uploadImage : null,
      uploadImageName: ''
    })
  }

  handleLoadingSend=()=>{
    this.setState({
      loadingSend : !this.state.loadingSend
    })
  }

  handleOpenUploadFile=()=>{
    this.setState({
      open : true,
    });
  }

  handleCloseUploadFile=()=>{
    this.setState({
      open : false,
    });
  }

  componentDidMount() {
    if (this.props.token) {
      axios.defaults.headers = {
        "Content-Type": "application.json",
        Authorization: "Token " + this.props.token,
      };
      axios.get(`https://${this.props.url}/userprofile/`).then((res) => {
        const prof = res.data[0];
        const username = prof.user;
        this.setState({
          teamName: prof.teamName,
          username: username,
          isactive: res.data.isactive,
        });
        axios
          .get(`https://${this.props.url}/userprofile_image/`)
          .then((res) => {
            const image = res.data[0];
            this.setState({
              image: image.image,
            });
          });
        axios
          .get(`https://${this.props.url}/comment/?teamName=${prof.teamName}`)
          .then((res) => {
            this.setState({
              conversation: res.data.reverse(),
            });
          });
        axios.get(`https://${this.props.url}/user_image`).then((res) => {
          this.setState({
            user_image: res.data,
            loading: false,
          });
        });
      });
      this.scrollToBottom();
    }
  }

  UNSAFE_componentWillReceiveProps(newProps) {
    if (newProps.token) {
      axios.defaults.headers = {
        "Content-Type": "application.json",
        Authorization: "Token " + newProps.token,
      };
      axios.get(`https://${this.props.url}/userprofile/`).then((res) => {
        const prof = res.data[0];
        const username = prof.user;
        this.setState({
          teamName: prof.teamName,
          username: username,
        });
        axios
          .get(`https://${this.props.url}/userprofile_image/`)
          .then((res) => {
            const image = res.data[0];
            this.setState({
              image: image.image,
            });
          });
        axios
          .get(`https://${this.props.url}/comment/?teamName=${prof.teamName}`)
          .then((res) => {
            this.setState({
              conversation: res.data.reverse(),
            });
          });
        axios.get(`https://${this.props.url}/user_image`).then((res) => {
          this.setState({
            user_image: res.data,
            loading: false,
          });
        });
      });
      this.scrollToBottom();
    }
  }

  componentDidUpdate() {
    this.scrollToBottom();
}
  scrollToBottom() {
      animateScroll.scrollToBottom({
        containerId: "ContainerElementID"
      });
  }

  handlechange = (event) => {
    this.setState({
      input: event.target.value,
    });
  };

  handleSubmit = (event, message ) => {
    event.preventDefault();
    this.handleLoadingSend();
    let form_data = new FormData();
    form_data.append("user", this.state.username);
    form_data.append("teamName", this.state.teamName);
    if(message){
    form_data.append("message", message);
    }
    if(this.state.uploadImage != null){
    form_data.append("files", this.state.uploadImage);}
    const url_post = `https://${this.props.url}/comment/`;
    axios.defaults.headers = {
      "Content-Type": "application.json",
      Authorization: "Token " + this.props.token,
    };
    axios
      .post(url_post, form_data, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((res) => {
        this.setState({
          input: "",
          conversation: [res.data, ...this.state.conversation],
          uploadImage: null
        });
        this.handleLoadingSend();
      })
      .catch((err) => console.log(err));
  };

  handleMessageUpdate = (data) => {
    this.handledata(data);
  };

  handletext = (data) => {
    this.setState({
      input: `${this.state.input}${data}`,
    });
  };

  handleActiveUserList = (data) => {
    this.setState({
      activeUsersList: data,
    });
  };

  handleLike = () => {
    this.setState({
      input: `${this.state.input}👍🏻`,
    });
  };

  handleSend = (event, message) => {
    if (message !== "") {
      this.handleSubmit(event, message);
    }
  };

  render() {
    console.log(this.state.uploadImageName);
    return (
      <MessageLists
        data={this.state}
        loading={this.state.loading}
        loading1={this.props.loading}
        scrollToBottom={this.scrollToBottom}
        handleUsers={this.handleUsers}
        handleActiveUserList={this.handleActiveUserList}
        url={this.props.url}
        token={this.props.token}
        handleLoadingSend={this.handleLoadingSend}
        handleMessageUpdate={this.handleMessageUpdate}
        handleSend={this.handleSend}
        handleLike={this.handleLike}
        handletext={this.handletext}
        toggleEmojiPicker={this.toggleEmojiPicker}
        handlechange={this.handlechange}
        title={this.state.input}
        handleImageUploadFile={this.handleImageUploadFile}
        handleSubmit={this.handleSubmit}
        handleOpenUploadFile={this.handleOpenUploadFile}
        handleCloseUploadFile={this.handleCloseUploadFile}
        handleClearImage={this.handleClearImage}
      />
    );
  }
}

const mapStateToProps = (state) => {
  return {
    token: state.token,
    url: state.baseurl,
  };
};

export default connect(mapStateToProps)(MessageList);
