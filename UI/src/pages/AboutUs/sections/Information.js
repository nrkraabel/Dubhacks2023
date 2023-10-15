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

// Material Kit 2 React components
import MKBox from "components/MKBox";

// Material Kit 2 React examples
import DefaultInfoCard from "examples/Cards/InfoCards/DefaultInfoCard";
import CenteredBlogCard from "examples/Cards/BlogCards/CenteredBlogCard";
import CenteredBlogCard2 from "examples/Cards/BlogCards/CenteredBlogCard2";

function Information() {
  return (
    <MKBox component="section" py={12}>
      <Container>
        <Grid container spacing={3} alignItems="center">
{/*           <Grid item xs={12} lg={6}>
            <Grid container justifyContent="flex-start">
              <Grid item xs={12} md={6}>
                <MKBox mb={5}>
                  <DefaultInfoCard
                    icon="public"
                    title="Fully integrated"
                    description="We get insulted by others, lose trust for those We get back freezes"
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} md={6}>
                <MKBox mb={5}>
                  <DefaultInfoCard
                    icon="payments"
                    title="Payments functionality"
                    description="We get insulted by others, lose trust for those We get back freezes"
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} md={6}>
                <MKBox mb={{ xs: 5, md: 0 }}>
                  <DefaultInfoCard
                    icon="apps"
                    title="Prebuilt components"
                    description="We get insulted by others, lose trust for those We get back freezes"
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} md={6}>
                <MKBox mb={{ xs: 5, md: 0 }}>
                  <DefaultInfoCard
                    icon="3p"
                    title="Improved platform"
                    description="We get insulted by others, lose trust for those We get back freezes"
                  />
                </MKBox>
              </Grid>
            </Grid>
          </Grid> */}
          <Grid item xs={12} lg={4} sx={{ height: '500px', ml: "auto", mt: { xs: 3, lg: 0 } }}  alignItems="stretch">
            <CenteredBlogCard2
              title="About Us"
              description="After countless tragic stories of families torn apart by war, I created a unique platform powered by advanced AI. This website isn't just technology; it's a beacon of hope, aiming to reunite loved ones separated by conflict. It's a blend of my passion for tech with a deep sense of empathy. Every reunion achieved is a testament to our shared human spirit. Let's reconnect the world, one family at a time." 
              action={{
                type: "internal",
                route: "pages/company/about-us",
                color: "info",
                label: "find out more",
                py: 20,
              }}
            />
          </Grid>
          <Grid item xs={12} lg={4} sx={{ height: '500px', ml: "auto", mt: { xs: 3, lg: 0 } }}  alignItems="stretch">
            <CenteredBlogCard
              image="https://images.unsplash.com/photo-1544717302-de2939b7ef71?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"
              title="Search a Missing Person"
              description="Uhh!"
              action={{
                type: "internal",
                route: "/find-form",
                color: "info",
                label: "Search Person",
              }}
            />
          </Grid>
          <Grid item xs={12} lg={4} sx={{height: '500px', ml: "auto", mt: { xs: 3, lg: 0 } }}>
            <CenteredBlogCard
              image="https://images.unsplash.com/photo-1544717302-de2939b7ef71?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80"
              title="Share an Image"
              description="Huh?"
              action={{
                type: "internal",
                route: "/upload-form",
                color: "info",
                label: "Share Images",
              }}
            />
          </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Information;
