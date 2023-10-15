/*
=========================================================
* Material Kit 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-kit-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import React, { Component } from 'react';
// Material Kit 2 React components
import MKBox from "components/MKBox";
import MKInput from "components/MKInput";
import MKButton from "components/MKButton";
import MKTypography from "components/MKTypography";

// Images
import bgImage from "assets/images/examples/blog2.jpg";
import GooglePicker from "./GooglePicker";

import { MagnifyingGlass } from 'react-loader-spinner'


export default class Contact extends Component {
    constructor(props) {
        super(props)
        this.state = { image_data: [], loading: false}
    }
    render() {
        if (this.state.loading) {

            return (
                <MKBox component="section" py={{ xs: 0, lg: 6 }}>
                    <Container>
                        <Grid container item>
                            <MKBox
                                width="100%"
                                bgColor="white"
                                borderRadius="xl"
                                shadow="xl"
                                mb={6}
                                sx={{ overflow: "hidden" }}
                            >
                                <Grid container spacing={2}>

                                    <Grid item xs={12} lg={12}>
                                        <MKBox component="form" p={2} method="post">
                                            <MKBox px={3} py={{ xs: 2, sm: 6 }}>
                                                <MKTypography
                                                    style={{ textAlign: "center" }}
                                                    variant="h2" mb={1}>
                                                    One Step Closer
                                                </MKTypography>
                                                <MKTypography style={{ textAlign: "center" }} variant="body1" color="text" mb={2}>
                                                    We Are Processing Your Search
                                                </MKTypography>
                                                <div style={{ margin: "auto", display: "block", width: "120px", height: "120px" }}>
                                                    <MagnifyingGlass
                                                        visible={true}
                                                        height="120"
                                                        width="120"
                                                        ariaLabel="MagnifyingGlass-loading"
                                                        wrapperStyle={{}}
                                                        wrapperClass="MagnifyingGlass-wrapper"
                                                        glassColor='#c0efff'
                                                        color='#e15b64'
                                                    />
                                                </div>
                                            </MKBox>
                                            <MKBox pt={0.5} pb={3} px={3}>
                                            </MKBox>
                                        </MKBox>
                                    </Grid>
                                </Grid>





                            </MKBox>
                        </Grid>
                    </Container>
                </MKBox>
            );
        }


        return (
            <MKBox component="section" py={{ xs: 0, lg: 6 }}>
                <Container>
                    <Grid container item>
                        <MKBox
                            width="100%"
                            bgColor="white"
                            borderRadius="xl"
                            shadow="xl"
                            mb={6}
                            sx={{ overflow: "hidden" }}
                        >
                            <Grid container spacing={2}>

                                <Grid item xs={12} lg={12}>
                                    <MKBox component="form" p={2} method="post">
                                        <MKBox px={3} py={{ xs: 2, sm: 6 }}>
                                            
                                            <MKTypography variant="body1" color="text" mb={2}>
                                                We Hope We Can Help
                                            </MKTypography>
                                        </MKBox>
                                        <MKBox pt={0.5} pb={3} px={3}>
                                            <Grid container>
                                                <Grid item xs={12} pr={1} mb={6}>
                                                    <MKInput
                                                        variant="standard"
                                                        label="Full Name"
                                                        placeholder="Full Name"
                                                        InputLabelProps={{ shrink: true }}
                                                        fullWidth
                                                    />
                                                </Grid>
                                                <Grid item xs={12} pr={1} mb={6}>
                                                    <MKInput
                                                        variant="standard"
                                                        label="Tell Us As Much As You Can"
                                                        placeholder="Who are they to you? How long have they been missing?"
                                                        InputLabelProps={{ shrink: true }}
                                                        fullWidth
                                                        multiline
                                                        rows={6}
                                                    />
                                                </Grid>
                                            </Grid>

                                            <GooglePicker receivedData={(inp) => {
                                                console.log(inp)
                                                if (inp.docs !== undefined && inp.docs.length > 0) {
                                                    console.log(inp.docs, this.state.data)
                                                    this.setState({ image_data: this.state.image_data.concat(inp.docs), loading: true })

                                                }
                                            }} />
                                           
                                        </MKBox>
                                    </MKBox>
                                </Grid>
                            </Grid>
                        </MKBox>
                    </Grid>
                </Container>
            </MKBox>
        );
    }
}


