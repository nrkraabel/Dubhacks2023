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
import MKButton from "components/MKButton";

// Material Kit 2 React examples
import DefaultNavbar from "examples/Navbars/DefaultNavbar";
import DefaultFooter from "examples/Footers/DefaultFooter";

// About Us page sections
import Information from "pages/AboutUs/sections/Information";
import Team from "pages/AboutUs/sections/Team";
import Featuring from "pages/AboutUs/sections/Featuring";
import Newsletter from "pages/AboutUs/sections/Newsletter";
import Footer from "pages/AboutUs/sections/Footer";
import Profile from "pages/AboutUs/sections/Profile";
// Images
import bgImage from "assets/images/world-points.jpeg";

function AboutUs() {
    return (
           <>
            <MKBox
                minHeight="75vh"
                width="100%"
                sx={{
                    backgroundImage: ({ functions: { linearGradient, rgba }, palette: { gradients } }) =>
                        `${linearGradient(
                            rgba(gradients.dark.main, 0.75),
                            rgba(gradients.dark.state, 0.75)
                        )}, url(${bgImage})`,
                    backgroundSize: "cover",
                    backgroundPosition: "center",
                    display: "grid",
                    placeItems: "center",
                }}
            >
                <Container>
                    <Grid
                        container
                        item
                        xs={12}
                        lg={8}
                        justifyContent="center"
                        alignItems="center"
                        flexDirection="column"
                        sx={{ mx: "auto", textAlign: "center" }}
                    >            <MKTypography
                        variant="h1"
                        color="white"
                        sx={({ breakpoints, typography: { size } }) => ({
                            [breakpoints.down("md")]: {
                                fontSize: size["3xl"],
                            },
                        })}
                    >
                            Helping you <span style={{ color: '#A0EEFF' }}>find</span> hope.
                        </MKTypography>
                        <MKTypography variant="body1" color="white" opacity={0.8} mt={1} mb={3}>
                            Helping you find the people most
                            <span style={{ color: '#A0EEFF' }}> important </span>
                            to you during the most
                            <span style={{ color: '#A0EEFF' }}> important </span>
                            times.
                        </MKTypography> 
                        <MKButton color="default" sx={{ color: ({ palette: { dark } }) => dark.main }}>
                            <a href="/find-form">Search For A Missing Person</a>
                        </MKButton>
                    </Grid>
                </Container>
            </MKBox>
            <Card
                sx={{
                    p: 2,
                    mx: { xs: 2, lg: 3 },
                    mt: -8,
                    mb: 4,
                    boxShadow: ({ boxShadows: { xxl } }) => xxl,
                }}
            >
                <Profile />
               
                <Featuring />
                <Newsletter />
            </Card>
            <MKBox pt={6} px={1} mt={6}>
                <Footer />
            </MKBox>
        </>
    );
  
}

export default AboutUs;

/*
return (
    <>
      <MKBox


        minHeight="60vh"
        width="100%"
        sx={{
          backgroundImage: ({ functions: { linearGradient, rgba }, palette: { gradients } }) =>
            `${linearGradient(
              rgba(0, 0, 0, 0.9),  // Dark overlay with 90% opacity
              rgba(0, 0, 0, 0.9)  // Dark overlay with 60% opacity
            )}, url(${bgImage})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          display: "grid",
          placeItems: "center",
                  
        '&::before': {  // Pseudo-element for the dark overlay
          content: '""',
          position: "absolute",
          top: 0,
          right: 0,
          bottom: 0,
          left: 0,
          backgroundColor: "rgba(0, 0, 0, 0.6)", // Dark overlay with 60% opacity
          zIndex: 1
        },

        '& > *': {  // To make sure content is rendered above the overlay
          zIndex: 2,
          position: "relative"
        }
        }}
      >
        <Container>
          <Grid
            container
            item
            xs={12}
            lg={8}
            justifyContent="center"
            alignItems="center"
            flexDirection="column"
            sx={{ mx: "auto", textAlign: "center" }}
          >
            <MKTypography
              variant="h1"
              color="white"
              sx={({ breakpoints, typography: { size } }) => ({
                [breakpoints.down("md")]: {
                  fontSize: size["3xl"],
                },
              })}
            >
              Helping you <span style={{ color: '#A0EEFF' }}>find</span> hope.
            </MKTypography>
            <MKTypography variant="body1" color="white" opacity={0.8} mt={1} mb={3}>
              Helping you find the people most 
              <span style={{ color: '#A0EEFF' }}> important </span> 
                people to you during the most 
              <span style={{ color: '#A0EEFF' }}> important </span> 
                times.
          </MKTypography>

          </Grid >
        </Container >
      </MKBox >
      <Card
        sx={{
          p: 2,
          mx: { xs: 2, lg: 3 },
          mt: -8,
          mb: 4,
          zIndex: 3,
          boxShadow: ({ boxShadows: { xxl } }) => xxl,
        }}
      >
        <Information />
         
      </Card>
      <Footer />
      
    </>
  );
*/