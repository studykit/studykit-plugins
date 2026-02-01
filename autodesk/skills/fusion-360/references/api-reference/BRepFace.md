# BRepFace Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Represent a connected region on a single geometric surface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepFace_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [convert](BRepFace_convert.htm) | Creates a new body where this face and its edges are converted to different types of geometry based on the input options. |
| [createForAssemblyContext](BRepFace_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [isPointOnFace](BRepFace_isPointOnFace.htm) | Checks if input point is on this BRepFace. This takes into account any boundaries so if the point is within a void area of the face, this will return false. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [appearance](BRepFace_appearance.htm) | Read-write property that gets and sets the current appearance of the face. Setting this property will result in applying an override appearance to the face and the AppearanceSourceType property will return OverrideAppearanceSource. Setting this property to null will remove any override. |
| [appearanceSourceType](BRepFace_appearanceSourceType.htm) | Read-write property that gets the source of the appearance for the face. If this returns OverrideAppearanceSource, an override exists on this face. The override can be removed by setting the Appearance property to null. |
| [area](BRepFace_area.htm) | Returns the area in cm ^ 2. |
| [assemblyContext](BRepFace_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepFace object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [attributes](BRepFace_attributes.htm) | Returns the collection of attributes associated with this face. |
| [body](BRepFace_body.htm) | Returns the parent body of the face. |
| [boundingBox](BRepFace_boundingBox.htm) | Returns the bounding box of this face |
| [centroid](BRepFace_centroid.htm) | Returns a point at the centroid (aka, geometric center) of the face. |
| [edges](BRepFace_edges.htm) | Returns the BRepEdges used by this face |
| [entityToken](BRepFace_entityToken.htm) | Returns a token for the BRepFace object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same face.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.   This is only valid for faces that exist in the design, (the isTemporary property is false). |
| [evaluator](BRepFace_evaluator.htm) | Returns a SurfaceEvaluator to allow geometric evaluations across the face's surface. This evaluator differs from the evaluator available from the Surface obtained from the geometry property by being bounded by the topological boundaries of this face. |
| [geometry](BRepFace_geometry.htm) | Returns the underlying surface geometry of this face |
| [isParamReversed](BRepFace_isParamReversed.htm) | Gets if the normal of this face is reversed with respect to the surface geometry associated with this face. |
| [isValid](BRepFace_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [loops](BRepFace_loops.htm) | Returns the BRepLoops owned by this face |
| [meshManager](BRepFace_meshManager.htm) | Returns a MeshManager object that allows access to existing and new meshes of this face. |
| [nativeObject](BRepFace_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BRepFace_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [pointOnFace](BRepFace_pointOnFace.htm) | Returns a sample point guaranteed to lie on the face's surface, within the face's boundaries, and not on a boundary edge. |
| [shell](BRepFace_shell.htm) | Returns the parent shell of the face. |
| [tangentiallyConnectedFaces](BRepFace_tangentiallyConnectedFaces.htm) | Returns the set of faces that are tangentially adjacent to this face. In other words, it is the set of faces that are adjacent to this face's edges and have a smooth transition across those edges. |
| [tempId](BRepFace_tempId.htm) | Returns the temporary ID of this face. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID. |
| [vertices](BRepFace_vertices.htm) | Returns the BRepVertices used by this face |

## Accessed From

[BRepFace.createForAssemblyContext](BRepFace_createForAssemblyContext.htm), [BRepFace.nativeObject](BRepFace_nativeObject.htm), [BRepFaces.item](BRepFaces_item.htm), [BRepLoop.face](BRepLoop_face.htm), [ConstructionAxisCircularFaceDefinition.circularFace](ConstructionAxisCircularFaceDefinition_circularFace.htm), [ConstructionAxisPerpendicularAtPointDefinition.face](ConstructionAxisPerpendicularAtPointDefinition_face.htm), [ConstructionPlaneTangentAtPointDefinition.tangentFace](ConstructionPlaneTangentAtPointDefinition_tangentFace.htm), [Decal.faces](Decal_faces.htm), [DecalInput.faces](DecalInput_faces.htm), [DeleteFaceFeature.deletedFaces](DeleteFaceFeature_deletedFaces.htm), [DraftFeature.inputFaces](DraftFeature_inputFaces.htm), [DraftFeatureInput.inputFaces](DraftFeatureInput_inputFaces.htm), [EmbossFeature.inputFaces](EmbossFeature_inputFaces.htm), [EmbossFeatureInput.inputFaces](EmbossFeatureInput_inputFaces.htm), [FaceRipFeatureDefinition.ripFace](FaceRipFeatureDefinition_ripFace.htm), [FlatPattern.bottomFace](FlatPattern_bottomFace.htm), [FlatPattern.topFace](FlatPattern_topFace.htm), [FullRoundFilletFaceSet.centerFace](FullRoundFilletFaceSet_centerFace.htm), [FullRoundFilletFaceSet.sideOneFaces](FullRoundFilletFaceSet_sideOneFaces.htm), [FullRoundFilletFaceSet.sideTwoFaces](FullRoundFilletFaceSet_sideTwoFaces.htm), [LoftFeature.endFace](LoftFeature_endFace.htm), [LoftFeature.startFace](LoftFeature_startFace.htm), [MergeFacesFeatureInput.inputFaces](MergeFacesFeatureInput_inputFaces.htm), [PatternElement.faces](PatternElement_faces.htm), [Profile.face](Profile_face.htm), [RecognizedPocket.faces](RecognizedPocket_faces.htm), [RecognizedPocket.sharedFaces](RecognizedPocket_sharedFaces.htm), [SurfaceDeleteFaceFeature.deletedFaces](SurfaceDeleteFaceFeature_deletedFaces.htm), [SweepFeature.guideSurfaces](SweepFeature_guideSurfaces.htm), [SweepFeatureInput.guideSurfaces](SweepFeatureInput_guideSurfaces.htm), [TangentRelationshipInput.faceOne](TangentRelationshipInput_faceOne.htm), [ThreadFeature.inputCylindricalFace](ThreadFeature_inputCylindricalFace.htm), [ThreadFeatureInput.inputCylindricalFace](ThreadFeatureInput_inputCylindricalFace.htm), [UntrimFeature.facesToUntrim](UntrimFeature_facesToUntrim.htm), [UntrimFeatureInput.facesToUntrim](UntrimFeatureInput_facesToUntrim.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |