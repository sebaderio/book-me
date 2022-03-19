import { useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";

function Copyright() {
  const navigate = useNavigate();

  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      onClick={() => navigate("/")}
    >
      Copyright © BookMe Inc. {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

function Footer(props) {
  return (
    <Box component="footer" sx={{ bgcolor: "background.paper", py: 6 }}>
      <Container maxWidth="lg">
        <Copyright />
      </Container>
    </Box>
  );
}

export default Footer;
