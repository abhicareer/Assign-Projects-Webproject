import React, { useState } from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import Card from "../../css/Card/Card";
import CardHeader from "../../css/Card/CardHeader.js";
import CardBody from "../../css/Card/CardBody.js";
import Switch from "@material-ui/core/Switch";
import Chip from "@material-ui/core/Chip";
import Loading from "../../../loading.js";

import {
  CardActions,
  TableBody,
  TableCell,
  TableRow,
  TablePagination,
  Table,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    padding: "10px",
    margin: "20px",
  },
  header: {
    background: (props) =>
      props.color === "red"
        ? "linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)"
        : "linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)",
    border: 0,
  },
  actions: {
    justifyContent: "flex-end",
  },
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0",
    flexGrow: 1,
  },
  gridList: {
    width: "100%",
    height: 610,
    transform: "translateZ(0)",
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none",
  },
  right: {
    flexGrow: 1,
  },
  fab: {
    margin: theme.spacing(1),
  },
  icon: {
    marginRight: theme.spacing(1),
  },
  ac: {
    padding: theme.spacing(1),
    background: "linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)",
  },
}));

const Pending = (props) => {
  const { data } = props;
  const classes = useStyles();

  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [page, setPage] = useState(0);
  function handleChangePage(event, newPage) {
    setPage(newPage);
  }

  function handleChangeRowsPerPage(event) {
    setRowsPerPage(+event.target.value);
    setPage(0);
  }

  function handleChipSearch(event,data) {
    event.stopPropagation();
    props.handleChipSearch(data);
  }
  return (
    <>
      <Card style={{ background: "#eeeeee" }}>
        <CardHeader
          color="primary"
          style={{
            boxShadow:
              "0 4px 20px 0 #21CBF3, 0 7px 10px -5px rgba(244, 67, 54,.4)",
            overflowX: "auto",
          }}
        >
          <h4 className={classes.cardTitleWhite}>To Do</h4>
          <p className={classes.cardCategoryWhite}>Pending Work</p>
        </CardHeader>
        <CardBody style={{ overflowX: "hidden" }}>
          <div spacing={1} className={classes.gridList}>
            {!props.loading ? (
              <Table>
                <TableBody>
                  {data
                    .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                    .map((data) => (
                      <TableRow key={data.id}>
                        <TableCell>
                          <ExpansionPanel>
                            <ExpansionPanelSummary
                              key={data.id}
                              expandIcon={<ExpandMoreIcon />}
                              aria-controls="panel1a-content"
                              id="panel1a-header"
                            >
                              <Typography
                                className={classes.heading}
                                style={{ flex: "auto" }}
                              >
                                {data.title}
                              </Typography>
                              <div>
                                {data.todochip.map((data1) => (
                                  <Chip
                                    onClick={(event) =>
                                      handleChipSearch(event,data1.chips)
                                    }
                                    key={data1.id}
                                    label={data1.chips}
                                    style={{ background: "lightskyblue" }}
                                  />
                                ))}
                              </div>
                            </ExpansionPanelSummary>
                            <ExpansionPanelDetails>
                              <Typography className={classes.right}>
                                {data.description}
                              </Typography>
                              <Switch
                                value="checkedC"
                                inputProps={{
                                  "aria-label": "primary checkbox",
                                }}
                                onClick={(event) =>
                                  props.handletoggle(
                                    this,
                                    data.id,
                                    data.title,
                                    data.description,
                                    data.completed
                                  )
                                }
                              />
                            </ExpansionPanelDetails>
                          </ExpansionPanel>
                        </TableCell>
                      </TableRow>
                    ))}
                </TableBody>
              </Table>
            ) : (
              <Loading />
            )}
          </div>
        </CardBody>
        <CardActions className={classes.actions}>
          <TablePagination
            rowsPerPageOptions={[5, 10, 25]}
            component="div"
            count={data.length}
            rowsPerPage={rowsPerPage}
            page={page}
            backIconButtonProps={{
              "aria-label": "previous page",
            }}
            nextIconButtonProps={{
              "aria-label": "next page",
            }}
            onChangePage={handleChangePage}
            onChangeRowsPerPage={handleChangeRowsPerPage}
          />
        </CardActions>
      </Card>
    </>
  );
};

Pending.propTypes = {
  className: PropTypes.string,
  data: PropTypes.array.isRequired,
};

export default Pending;
