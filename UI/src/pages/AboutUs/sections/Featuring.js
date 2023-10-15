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
import DefaultCounterCard from "examples/Cards/CounterCards/DefaultCounterCard";

// Images
import coinbase from "assets/images/logos/gray-logos/logo-coinbase.svg";
import nasa from "assets/images/logos/gray-logos/logo-nasa.svg";
import netflix from "assets/images/logos/gray-logos/logo-netflix.svg";
import pinterest from "assets/images/logos/gray-logos/logo-pinterest.svg";
import spotify from "assets/images/logos/gray-logos/logo-spotify.svg";
import vodafone from "assets/images/logos/gray-logos/logo-vodafone.svg";

function Featuring() {
  return (
    <MKBox component="section" pt={3} pb={8}>
      <Container>

        <Grid container justifyContent="center" sx={{ textAlign: "center" }}>
          <Grid item xs={12} md={3}>
            <DefaultCounterCard
               count={546568}
              separator=","
              title="Missing People"
              description="In The US In 2022"
            />
          </Grid>
            <Grid item xs={12} md={3}>
                <DefaultCounterCard
                    count={60000}
                    separator=","
                    title="Dissapeared Without A Trace"
                          description="In The Russia-Ukraine War (Approximately)"
                />
            </Grid>
            <Grid item xs={12} md={3}>
                <DefaultCounterCard
                    count={840000}
                    separator=","
                    title="Missing Children"
                          description="Estimated Each Year By FBI"
                />
            </Grid>
        </Grid>
      </Container>
    </MKBox>
  );
}

export default Featuring;
