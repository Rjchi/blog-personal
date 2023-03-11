import { Link, useLocation } from "react-router-dom";

const BlogCateHeader = ({ categories }) => {
  // Esto nos da un objeto y este objeto contiene el path
  const location = useLocation();

  return (
    <div className="mx-auto max-w-6xl py-12 px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-12">
        <div className="col-span-9">
          <div className="space-x-8 px-2">
            <div className="relative">
              <div className="relative -mb-6 w-full overflow-x-auto pb-6">
                <ul className="mx-4 inline-flex space-x-8 sm:mx-6">
                  <Link
                  to="/blog"
                    className={`${
                      location.pathname === "/blog"
                        ? "text-purple-800 bg-gray-50 border border-purple-800"
                        : "text-gray-900 border hover:text-purple-800 hover:border-purple-800"
                    } inline-flex flex-col text-center lg:w-auto py-2 px-4 text-gray-900 text-md font-medium rounded`}
                  >
                    All
                  </Link>
                  {categories &&
                    categories.map((category) => (
                      <Link
                      key={category.id}
                      to={`/category/${category.slug}`}
                        className={`${
                          location.pathname === `/category/${category.slug}`
                            ? "text-purple-800 bg-gray-50 border border-purple-800"
                            : "text-gray-900 border hover:text-purple-800 hover:border-purple-800"
                        } inline-flex flex-col text-center lg:w-auto py-2 px-4 text-gray-900 text-md font-medium rounded`}
                      >
                        {category.name}
                      </Link>
                    ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div className="col-span-3 bg-gray-400">search</div>
      </div>
    </div>
  );
};

export default BlogCateHeader;
