import CssBaseline from "@mui/material/CssBaseline";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Footer from "../components/Footer";
import { withStyles } from "@mui/styles";

import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { useNavigate } from "react-router-dom";

const theme = createTheme();

const BlueTextTypography = withStyles({
  root: {
    color: "#1976d2",
  },
})(Typography);

export default function NotFoundPage() {
  const navigate = useNavigate();

  return (
    <ThemeProvider theme={theme}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          minHeight: "100vh",
        }}
      >
        <CssBaseline />
        <Container component="main" sx={{ mt: 8, mb: 2 }} maxWidth="sm">
          <Typography variant="h2" component="h1" gutterBottom>
            404
          </Typography>
          <Typography variant="h5" component="h2" gutterBottom>
            Sorry, but the page you are looking for does not exist, has been
            removed, name changed or is temporarily unavailable.
          </Typography>
          <BlueTextTypography variant="body1" onClick={() => navigate("/")}>
            Back to homepage
          </BlueTextTypography>
        </Container>
        <Footer />
      </Box>
    </ThemeProvider>
  );
}
