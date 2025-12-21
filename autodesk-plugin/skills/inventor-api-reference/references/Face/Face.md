# Face Object

## Description

The Face object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateFacets](../Face/Face_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. |
| [CalculateFacetsAndTextureMap](../Face/Face_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. This also include the texture map coordinates. |
| [CalculateFacetsWithOptions](../Face/Face_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../Face/Face_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. |
| [CalculateStrokesWithOptions](../Face/Face_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetClosestPointTo](../Face/Face_GetClosestPointTo.md) | Method that returns a point on the face that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u-v parameters of the returned point on the face, use Face.Evaluator.GetParamAtPoint method. |
| [GetExistingFacets](../Face/Face_GetExistingFacets.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetsAndTextureMap](../Face/Face_GetExistingFacetsAndTextureMap.md) | Method that returns the specified set of existing display facets. Existing display facets are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateFacets method which will calculate new facets to a given tolerance at double-precision accuracy. |
| [GetExistingFacetTolerances](../Face/Face_GetExistingFacetTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to facets. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokes](../Face/Face_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../Face/Face_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetReferenceKey](../Face/Face_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceFace](../Face/Face_GetSourceFace.md) | Method that gets the source face that has been overridden by this face. The method returns Nothing if this face is not an override. An error is returned if this method is called on a face in a part. |
| [GetTextureScale](../Face/Face_GetTextureScale.md) | Method that returns U scale and V scale. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlternateBody](../Face/Face_AlternateBody.md) | Property that returns the alternate SurfaceBody. |
| [Appearance](../Face/Face_Appearance.md) | Gets and sets the current appearance of the face. |
| [AppearanceSourceType](../Face/Face_AppearanceSourceType.md) | Gets and sets the source of the appearance for the face. |
| [Application](../Face/Face_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Face/Face_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CreatedByFeature](../Face/Face_CreatedByFeature.md) | Property that returns the feature that resulted in the creation of this face. This property is not currently supported for FaceProxy objects and will return Nothing in those cases. It is also not currently supported for Assembly Features and will fail in that case. |
| [EdgeLoops](../Face/Face_EdgeLoops.md) | Gets the EdgeLoops collection referenced by this Face. |
| [Edges](../Face/Face_Edges.md) | Gets the Edges referenced by this Face. |
| [Evaluator](../Face/Face_Evaluator.md) | Gets the surface evaluator for this face. |
| [FaceShell](../Face/Face_FaceShell.md) | Property that returns the FaceShell object. |
| [Geometry](../Face/Face_Geometry.md) | Property that returns the underlying geometry of the face. |
| [GeometryForm](../Face/Face_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [HasReferenceComponent](../Face/Face_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [InternalName](../Face/Face_InternalName.md) | Property that returns a unique string identifying this face. This identifier is valid only so long as there are no further modifications to the face. |
| [IsParamReversed](../Face/Face_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this Face. |
| [Parent](../Face/Face_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PointOnFace](../Face/Face_PointOnFace.md) | Property that returns a characteristic somewhere on the interior of the Face. |
| [ReferenceComponent](../Face/Face_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../Face/Face_ReferencedEntity.md) | Property that returns the referenced face(s) from the source part. This could be a proxy object in case of a derived assembly. The property returns Nothing if there isn't a referenced entity. |
| [SurfaceBody](../Face/Face_SurfaceBody.md) | Property that returns the associated with this object or feature. |
| [SurfaceType](../Face/Face_SurfaceType.md) | Property that returns a SurfaceTypeEnum that specifies the surface type for this Face. |
| [TangentiallyConnectedFaces](../Face/Face_TangentiallyConnectedFaces.md) | Property that returns a FaceCollection that contains the input face and all tangentially connected faces. The CollectionType of the output FaceCollection is set to kFaceTangentiallyConnected. |
| [TextureMaps](../Face/Face_TextureMaps.md) | Gets the texture maps associated with this face. |
| [ThreadInfos](../Face/Face_ThreadInfos.md) | Property that returns a ThreadInfo object for each thread affecting this face. |
| [TransientKey](../Face/Face_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../Face/Face_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vertices](../Face/Face_Vertices.md) | Gets the vertices for this Face. |

## Accessed From

[ASideDefinition.ASideFace](../ASideDefinition/ASideDefinition_ASideFace.md), [ChamferDefinition.Face](../ChamferDefinition/ChamferDefinition_Face.md), [DecalFeature.Face](../DecalFeature/DecalFeature_Face.md), [DecalFeatureProxy.Face](../DecalFeatureProxy/DecalFeatureProxy_Face.md), [DistanceAndAngleChamferDef.Face](DistanceAndAngleChamferDef_Face.md), [EdgeLoop.Face](../EdgeLoop/EdgeLoop_Face.md), [EdgeLoopProxy.Face](../EdgeLoopProxy/EdgeLoopProxy_Face.md), [EmbossFeature.WrapFace](../EmbossFeature/EmbossFeature_WrapFace.md), [EmbossFeatureProxy.WrapFace](../EmbossFeatureProxy/EmbossFeatureProxy_WrapFace.md), [Face.GetSourceFace](../Face/Face_GetSourceFace.md), [FaceProxy.GetSourceFace](../FaceProxy/FaceProxy_GetSourceFace.md), [FaceProxy.NativeObject](../FaceProxy/FaceProxy_NativeObject.md), [Faces.Item](../Faces/Faces_Item.md), [FlatPattern.BaseFace](../FlatPattern/FlatPattern_BaseFace.md), [FlatPattern.BottomFace](../FlatPattern/FlatPattern_BottomFace.md), [FlatPattern.TopFace](../FlatPattern/FlatPattern_TopFace.md), [LineAndFaceWorkPointDef.Face](LineAndFaceWorkPointDef_Face.md), [LineAndFaceWorkPointDef.GetData](LineAndFaceWorkPointDef_GetData.md), [LineAndTangentWorkPlaneDef.Face](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Face.md), [LineAndTangentWorkPlaneDef.GetData](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_GetData.md), [LoftFeature.EndFace](../LoftFeature/LoftFeature_EndFace.md), [LoftFeature.StartFace](../LoftFeature/LoftFeature_StartFace.md), [LoftFeatureProxy.EndFace](../LoftFeatureProxy/LoftFeatureProxy_EndFace.md), [LoftFeatureProxy.StartFace](../LoftFeatureProxy/LoftFeatureProxy_StartFace.md), [MeshFace.Face](../MeshFace/MeshFace_Face.md), [MeshFaceProxy.Face](../MeshFaceProxy/MeshFaceProxy_Face.md), [MidSurfaceThickness.GetSourceFace](MidSurfaceThickness_GetSourceFace.md), [PlaneAndTangentWorkPlaneDef.Face](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Face.md), [PlaneAndTangentWorkPlaneDef.GetData](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_GetData.md), [PointAndTangentWorkPlaneDef.Face](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Face.md), [PointAndTangentWorkPlaneDef.GetData](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_GetData.md), [PublicationMeshFace.Face](PublicationMeshFace_Face.md), [RefoldFeature.StationaryFace](../RefoldFeature/RefoldFeature_StationaryFace.md), [RefoldFeatureProxy.StationaryFace](../RefoldFeatureProxy/RefoldFeatureProxy_StationaryFace.md), [RevolvedFaceWorkAxisDef.Face](../RevolvedFaceWorkAxisDef/RevolvedFaceWorkAxisDef_Face.md), [RipDefinition.RipFace](../RipDefinition/RipDefinition_RipFace.md), [RuledSurfaceEdgeFacePair.GetData](../RuledSurfaceEdgeFacePair/RuledSurfaceEdgeFacePair_GetData.md), [SphereCenterPointWorkPointDef.Face](../SphereCenterPointWorkPointDef/SphereCenterPointWorkPointDef_Face.md), [SurfaceGraphicsFace.Face](../SurfaceGraphicsFace/SurfaceGraphicsFace_Face.md), [TorusCenterPointWorkPointDef.Face](../TorusCenterPointWorkPointDef/TorusCenterPointWorkPointDef_Face.md), [TorusMidPlaneWorkPlaneDef.Face](../TorusMidPlaneWorkPlaneDef/TorusMidPlaneWorkPlaneDef_Face.md), [TwoDistancesChamferDef.Face](TwoDistancesChamferDef_Face.md), [UnfoldFeature.StationaryFace](../UnfoldFeature/UnfoldFeature_StationaryFace.md), [UnfoldFeatureProxy.StationaryFace](../UnfoldFeatureProxy/UnfoldFeatureProxy_StationaryFace.md)

## Derived Classes

[FaceProxy](../FaceProxy/FaceProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 4
