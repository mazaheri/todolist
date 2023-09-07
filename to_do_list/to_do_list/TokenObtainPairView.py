from datetime import datetime

import jwt  # Import the JWT library
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Calculate remaining token lifetime in seconds
            access_token = response.data.get('access')
            if access_token:
                # Decode the JWT token to access its payload
                decoded_token = jwt.decode(access_token, options={"verify_signature": False})

                # Get the expiration timestamp from the payload
                exp_timestamp = decoded_token['exp']

                # Calculate remaining lifetime
                current_timestamp = datetime.timestamp(datetime.now())
                remaining_lifetime = exp_timestamp - current_timestamp

                remaining_minutes = remaining_lifetime // 60
                remaining_seconds = int(remaining_lifetime % 60)

                # Add 'expires_in_minutes' and 'expires_in_seconds' to the response data
                response.data['expires_in_minutes'] = int(remaining_minutes)
                response.data['expires_in_seconds'] = remaining_seconds

                # Convert remaining lifetime to seconds
                response.data['total_expiration_in_seconds'] = int(remaining_lifetime)
        return response
