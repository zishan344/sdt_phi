import { useEffect, useState } from "react";
import { useParams } from "react-router";
import authApiClient from "../../services/auth-api-client";
import ReviewForm from "./ReviewForm";
import StarRating from "./StarRating";

const ReviewSection = () => {
  const { productId } = useParams();
  const [userCanReview, setUserCanReview] = useState(false);

  const onSubmit = async (data) => {
    console.log(data);
    try {
      const res = await authApiClient.post(
        `/products/${productId}/reviews/`,
        data
      );
      console.log(res.data);
    } catch (error) {
      console.log("Error submitting reviews", error);
    }
  };

  const checkUserPermission = async () => {
    try {
      const res = await authApiClient.get(`/orders/has-ordered/${productId}/`);
      setUserCanReview(res.data.hasOrdered);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    checkUserPermission();
  }, []);

  return (
    <div>
      <div>
        {userCanReview && <StarRating onChange={onSubmit} rating={5} />}
      </div>
      <div>{userCanReview && <ReviewForm onSubmit={onSubmit} />}</div>
    </div>
  );
};

export default ReviewSection;
