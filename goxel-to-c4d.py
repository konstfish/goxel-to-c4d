import c4d

def main():
    f=open('/Users/david/Desktop/goxel-to-c4d/fish.txt', 'r')
    t=f.readlines()
    f.close()

    # Generates matrices and colors for 100 instances
    for l in t:
        if(not l.startswith("#")):
            inf = l.split(" ")

            obj = c4d.BaseObject(c4d.Ocube)

            obj.SetRelPos(c4d.Vector(int(inf[0]) * 20, int(inf[1]) * 20, int(inf[2]) * 20))
            obj.SetRelScale(c4d.Vector(0.1, 0.1, 0.1))
            doc.InsertObject(obj)

            mat = c4d.Material()
            mat.RemoveReflectionLayerIndex(0)
            color = mat[c4d.MATERIAL_COLOR_COLOR]

            #res = c4d.modules.colorchooser.ColorHarmonyGetComplementary(color, False)
            #print(res)

            he = inf[3]
            print(he)

            r, g, b = he[:2], he[2:4], he[4:]
            r, g, b = [int(n, 16) for n in (r, g, b)]
            print(str(float(r) / 255.0) + " " + str(float(g) / 255.0) + " " + " " + str(float(b) / 255.0))



            mat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(float(r) / 255.0,float(g) / 255.0,float(b) / 255.0)

            doc.InsertMaterial(mat)

            textureTag = obj.MakeTag(c4d.Ttexture)
            textureTag[c4d.TEXTURETAG_MATERIAL] = mat

            c4d.EventAdd()

    c4d.EventAdd()
