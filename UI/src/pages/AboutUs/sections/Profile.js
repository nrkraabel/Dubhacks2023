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
import Icon from "@mui/material/Icon";

// Material Kit 2 React components
import MKBox from "components/MKBox";
import MKAvatar from "components/MKAvatar";
import MKButton from "components/MKButton";
import MKTypography from "components/MKTypography";

// Images
import profilePicture from "assets/images/bruce-mars.jpg";

function Profile() {
  return (
    <MKBox component="section" py={{ xs: 6, sm: 12 }}>
      <Container>
        <Grid container item xs={12} justifyContent="center" mx="auto">
          <Grid container justifyContent="center" py={6}>
            <Grid item xs={12} md={7} mx={{ xs: "auto", sm: 6, md: 1 }}>
              <MKBox display="flex" justifyContent="space-between" alignItems="center" mb={1}>
                <MKTypography variant="h3">What is FindingHope?</MKTypography>
              </MKBox>
              <MKTypography variant="body1" fontWeight="light" color="text">
                              <p>FindingHope is an AI-powered technology designed to support the search for missing war refugees, hostages, and other missing people. 
                              </p> <p><br/>
                              The key to FindingHope is understanding the power of everyday videos and pictures. Often, missing persons can unknowingly appear in the background of casual photos or videos taken by others. By allowing access to these everyday images, you're aiding a global mission to locate these individuals
                              </p> <p><br />
                              But we cannot accomplish this alone. Your involvement is critical to the success of FindingHope. By granting access to your camera roll, you are propelling a global search engine that can potentially reunite lost individuals with their families. Your contribution, coupled with our AI technology, can make a significant difference in finding hope for the missing.
                              </p>
                                  <MKTypography
                  component="a"
                  href="#"
                  variant="body1"
                  fontWeight="light"
                  color="info"
                  mt={3}
                  sx={{
                    width: "max-content",
                    display: "flex",
                    alignItems: "center",

                    "& .material-icons-round": {
                      transform: `translateX(3px)`,
                      transition: "transform 0.2s cubic-bezier(0.34, 1.61, 0.7, 1.3)",
                    },

                    "&:hover .material-icons-round, &:focus .material-icons-round": {
                      transform: `translateX(6px)`,
                    },
                  }}
                >
                                  <a href="/upload-form">Upload Today <Icon sx={{ fontWeight: "bold" }}>arrow_forward</Icon></a>
                </MKTypography>
              </MKTypography>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Profile;
