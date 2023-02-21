import { useEffect } from "react";

import { Helmet } from "react-helmet-async";

import Footer from "components/navegation/Footer";
import Navbar from "components/navegation/Navbar";

import Layout from "hocs/layouts/Layout";

// categories es un action de redux
import { get_categories } from "redux/actions/categories/categories";

import { connect } from "react-redux";

const Blog = ({ get_categories, categories }) => {
  useEffect(() => {
    window.scrollTo(0, 0)
    get_categories()
  }, []);

  return (
    <Layout>
      <Helmet>
        <title>Prototype | Blog</title>
        <meta
          name="description"
          content="Prototipo pagina web react y django (con fines educativos)"
        />
        <meta
          name="keywords"
          content="react & django, react y django, full stack web developer"
        />
        <meta name="robots" content="all" />
        <link rel="canonical" href="" />
        <meta name="author" content="Richi" />
        <meta name="publisher" content="Richi" />

        {/* Social Media Tags */}
        <meta property="og:title" content="Prototype" />
        <meta
          property="og:description"
          content="Prototipo pagina web react y django (con fines educativos)."
        />
        <meta property="og:url" content="" />
        <meta property="og:image" content="" />

        <meta name="twitter:title" content="Prototype" />
        <meta
          name="twitter:description"
          content="Prototipo pagina web react y django (con fines educativos)."
        />
        <meta name="twitter:image" content="" />
        <meta name="twitter:card" content="summary_large_image" />
      </Helmet>
      <Navbar />
      <div className="pt-28">Blog</div>
      <Footer />
    </Layout>
  );
};
const mapStateToProps = state => ({
  categories: state.categories.categories,
});

export default connect(mapStateToProps, {
  get_categories
})(Blog);
