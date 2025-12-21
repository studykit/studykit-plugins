# FaceProxy Object

Derived from: [Face](../Face/Face.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateFacets](../FaceProxy/FaceProxy_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. |
| [CalculateFacetsAndTextureMap](../FaceProxy/FaceProxy_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. This also include the texture map coordinates. |
| [CalculateFacetsWithOptions](../FaceProxy/FaceProxy_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../FaceProxy/FaceProxy_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. |
| [CalculateStrokesWithOptions](../FaceProxy/FaceProxy_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetClosestPointTo](../FaceProxy/FaceProxy_GetClosestPointTo.md) | Method that returns a point on the face that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u-v parameters of the returned point on the face, use Face.Evaluator.GetParamAtPoint method. |
| [GetExistingFacets](../FaceProxy/FaceProxy_GetExistingFacets.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetsAndTextureMap](../FaceProxy/FaceProxy_GetExistingFacetsAndTextureMap.md) | Method that returns the specified set of existing display facets. Existing display facets are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateFacets method which will calculate new facets to a given tolerance at double-precision accuracy. |
| [GetExistingFacetTolerances](../FaceProxy/FaceProxy_GetExistingFacetTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to facets. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokes](../FaceProxy/FaceProxy_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../FaceProxy/FaceProxy_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetReferenceKey](../FaceProxy/FaceProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceFace](../FaceProxy/FaceProxy_GetSourceFace.md) | Method that gets the source face that has been overridden by this face. The method returns Nothing if this face is not an override. An error is returned if this method is called on a face in a part. |
| [GetTextureScale](../FaceProxy/FaceProxy_GetTextureScale.md) | Method that returns U scale and V scale. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlternateBody](../FaceProxy/FaceProxy_AlternateBody.md) | Property that returns the alternate SurfaceBody. |
| [Appearance](../FaceProxy/FaceProxy_Appearance.md) | Gets and sets the current appearance of the face. |
| [AppearanceSourceType](../FaceProxy/FaceProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the face. |
| [Application](../FaceProxy/FaceProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FaceProxy/FaceProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../FaceProxy/FaceProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CreatedByFeature](../FaceProxy/FaceProxy_CreatedByFeature.md) | Property that returns the feature that resulted in the creation of this face. This property is not currently supported for FaceProxy objects and will return Nothing in those cases. It is also not currently supported for Assembly Features and will fail in that case. |
| [EdgeLoops](../FaceProxy/FaceProxy_EdgeLoops.md) | Gets the EdgeLoops collection referenced by this Face. |
| [Edges](../FaceProxy/FaceProxy_Edges.md) | Gets the Edges referenced by this Face. |
| [Evaluator](../FaceProxy/FaceProxy_Evaluator.md) | Gets the surface evaluator for this face. |
| [FaceShell](../FaceProxy/FaceProxy_FaceShell.md) | Property that returns the FaceShell object. |
| [Geometry](../FaceProxy/FaceProxy_Geometry.md) | Property that returns the underlying geometry of the face. |
| [GeometryForm](../FaceProxy/FaceProxy_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [HasReferenceComponent](../FaceProxy/FaceProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [InternalName](../FaceProxy/FaceProxy_InternalName.md) | Property that returns a unique string identifying this face. This identifier is valid only so long as there are no further modifications to the face. |
| [IsParamReversed](../FaceProxy/FaceProxy_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this Face. |
| [NativeObject](../FaceProxy/FaceProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../FaceProxy/FaceProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PointOnFace](../FaceProxy/FaceProxy_PointOnFace.md) | Property that returns a characteristic somewhere on the interior of the Face. |
| [ReferenceComponent](../FaceProxy/FaceProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../FaceProxy/FaceProxy_ReferencedEntity.md) | Property that returns the referenced face(s) from the source part. This could be a proxy object in case of a derived assembly. The property returns Nothing if there isn't a referenced entity. |
| [SurfaceBody](../FaceProxy/FaceProxy_SurfaceBody.md) | Property that returns the associated with this object or feature. |
| [SurfaceType](../FaceProxy/FaceProxy_SurfaceType.md) | Property that returns a SurfaceTypeEnum that specifies the surface type for this Face. |
| [TangentiallyConnectedFaces](../FaceProxy/FaceProxy_TangentiallyConnectedFaces.md) | Property that returns a FaceCollection that contains the input face and all tangentially connected faces. The CollectionType of the output FaceCollection is set to kFaceTangentiallyConnected. |
| [TextureMaps](../FaceProxy/FaceProxy_TextureMaps.md) | Gets the texture maps associated with this face. |
| [ThreadInfos](../FaceProxy/FaceProxy_ThreadInfos.md) | Property that returns a ThreadInfo object for each thread affecting this face. |
| [TransientKey](../FaceProxy/FaceProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../FaceProxy/FaceProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vertices](../FaceProxy/FaceProxy_Vertices.md) | Gets the vertices for this Face. |

## Version

Introduced in version 4
