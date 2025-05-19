import React from "react";
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

export default function Ganancias() {
  return (
    <>
      <DashboardNavbar />
      <MDBox p={3}>
        <MDTypography variant="h4" fontWeight="bold">
          Ganancias
        </MDTypography>
      </MDBox>
      <Footer />
    </>
  );
}
