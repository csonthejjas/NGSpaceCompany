# -*- coding: utf-8 -*-

from api.views._base import *
        
        
        
################################################################################
class RanksView(APIView):
    permission_classes = (AllowAny, )
    
	#---------------------------------------------------------------------------
    def get(self, request):
        #-----------------------------------------------------------------------
        dbConnect()
        #-----------------------------------------------------------------------
        data = dbRows("SELECT username, level, needed, remaining FROM ngsp_ranks JOIN auth_user ON ngsp_ranks.user_id = auth_user.id ORDER BY level DESC, remaining")
        #-----------------------------------------------------------------------
        return Response(data)
        #-----------------------------------------------------------------------
