class SendVerifyAgainView(APIView):

    def post(self, request):
        data = request.data.copy()
        serializer = AuthSerializer(data=data)
        serializer.is_valid(True)
        user = authenticate(serializer.validated_data['email'], serializer.validated_data['password'])
        if not user:
            raise exceptions.NotFound('User not found')
        code = VerifyCode.generate(6, user).code
        send_mail(
            'Koper Bank',
            f'{code} is your code',
            'no-reply@koper.pw',
            [user.email],
            fail_silently=False,
        )
        return Response(status=204)

class VerifyView(APIView):

    def patch(self, request):
        if 'code' not in request.data:
            raise exceptions.BadRequest("Enter code")
        code = request.data['code']
        code = VerifyCode.verify(code, None)
        if not code:
            raise exceptions.BadRequest("Code not found or expired")
        user = code.user
        user.is_active = True
        user.save()
        return Response(UserSerializer(user).data)

code = VerifyCode.generate(6, user).code
        send_mail(
            'Koper Bank',
            f'{code} is your code',
            'no-reply@koper.pw',
            [user.email],
            fail_silently=False,
        )