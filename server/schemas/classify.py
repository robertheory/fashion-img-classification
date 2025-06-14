from pydantic import BaseModel, Field


class ImageUploadForm(BaseModel):
    image: str = Field(...,
                       description="Image file uploaded via multipart/form-data")


class ImageUploadRequest(BaseModel):
    """Schema for image upload via multipart/form-data."""
    image: bytes = Field(...,
                         description="Image file uploaded via multipart/form-data")


class ImageClassificationRequest(BaseModel):
    """Define the request model for image classification (base64)."""
    image: str = Field(..., description="Base64 encoded image data",
                       example="iVBORw0KGgoAAAANSUhEUgAA...")


class ImageClassificationResponse(BaseModel):
    """Define the response model for image classification."""
    image_base64: str
