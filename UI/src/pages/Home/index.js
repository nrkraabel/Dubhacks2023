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
import Card from "@mui/material/Card";

// Material Kit 2 React components
import MKBox from "components/MKBox";
import MKTypography from "components/MKTypography";
import MKSocialButton from "components/MKSocialButton";

// Material Kit 2 React examples
import DefaultNavbar from "examples/Navbars/DefaultNavbar";
import DefaultFooter from "examples/Footers/DefaultFooter";
import FilledInfoCard from "examples/Cards/InfoCards/FilledInfoCard";

// Home page sections
import Counters from "pages/Home/sections/Counters";
import Information from "pages/Home/sections/Information";
import DesignBlocks from "pages/Home/sections/DesignBlocks";
import Pages from "pages/Home/sections/Pages";
import Testimonials from "pages/Home/sections/Testimonials";
import Download from "pages/Home/sections/Download";

// Home page components
import BuiltByDevelopers from "pages/Home/components/BuiltByDevelopers";



// Images
import bgImage from "assets/images/world-points.jpeg";

function Home() {
    return (
        <>

            <MKBox
                minHeight="75vh"
                width="100%"
                sx={{
                    backgroundImage: `url(${bgImage})`,
                    backgroundSize: "cover",
                    backgroundPosition: "top",
                    display: "grid",
                    placeItems: "center",
                }}
            >
                <Container>
                    <Grid container item xs={12} lg={7} justifyContent="center" mx="auto">
                        <MKTypography
                            variant="h1"
                            color="white"
                            mt={-6}
                            mb={1}
                            sx={({ breakpoints, typography: { size } }) => ({
                                [breakpoints.down("md")]: {
                                    fontSize: size["3xl"],
                                },
                            })}
                        >
                            FindingHope{" "}
                        </MKTypography>
                        <MKTypography
                            variant="body1"
                            color="white"
                            textAlign="center"
                            px={{ xs: 6, lg: 12 }}
                            mt={1}
                        >
                            Free & Open Source Web UI Kit built over ReactJS &amp; MUI. Join over 1.6 million
                            developers around the world.
                        </MKTypography>
                    </Grid>
                </Container>
            </MKBox>
            <Card
                sx={{
                    p: 2,
                    mx: { xs: 2, lg: 3 },
                    mt: -8,
                    mb: 4,
                    backgroundColor: ({ palette: { white }, functions: { rgba } }) => rgba(white.main, 0.8),
                    backdropFilter: "saturate(200%) blur(30px)",
                    boxShadow: ({ boxShadows: { xxl } }) => xxl,
                }}
            >

                <Container>

                    <Grid container spacing={6} >
                        <Grid item xs={12} lg={4} style={{height: '400px'}}>
                            <FilledInfoCard
                                color="info"
                                icon="precision_manufacturing"
                                title="Plugins"
                                description="About our stuff."
                                action={{
                                    type: "external",
                                    route: "https://www.creative-tim.com/learning-lab/react/overview/datepicker/",
                                    label: "Read more",
                                }}
                            />
                        </Grid>
                        <Grid item xs={12} lg={4} style={{height: '400px'}}>
                            <FilledInfoCard
                                variant="gradient"
                                color="info"
                                icon="flag"
                                title="Getting Started"
                                description="Search a person."
                                action={{
                                    type: "external",
                                    route: "/find-form",
                                    label: "Let's start",
                                }}
                            />
                        </Grid>
                        <Grid item xs={12} lg={4} style={{height: '400px'}}>
                            <FilledInfoCard
                                color="info"
                                icon="precision_manufacturing"
                                title="Plugins"
                                description="Share Images."
                                action={{
                                    type: "external",
                                    route: "https://www.creative-tim.com/learning-lab/react/overview/datepicker/",
                                    label: "Read more",
                                }}
                            />
                        </Grid>
                    </Grid>
                </Container>

            </Card>
            <MKBox pt={6} px={1} mt={6}>

            </MKBox>
        </>
    );
}

export default Home;
