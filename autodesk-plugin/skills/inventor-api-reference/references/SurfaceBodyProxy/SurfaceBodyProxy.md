# SurfaceBodyProxy Object

Derived from: [SurfaceBody](../SurfaceBody/SurfaceBody.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BindTransientKeyToObject](../SurfaceBodyProxy/SurfaceBodyProxy_BindTransientKeyToObject.md) | Bind the transient key of a subentity on this body to a live object. |
| [CalculateFacets](../SurfaceBodyProxy/SurfaceBodyProxy_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsAndTextureMap](../SurfaceBodyProxy/SurfaceBodyProxy_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsWithOptions](../SurfaceBodyProxy/SurfaceBodyProxy_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../SurfaceBodyProxy/SurfaceBodyProxy_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree. |
| [CalculateStrokesWithOptions](../SurfaceBodyProxy/SurfaceBodyProxy_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [ClearAppearanceOverrides](../SurfaceBodyProxy/SurfaceBodyProxy_ClearAppearanceOverrides.md) | Method that clears all the appearance overrides that have been applied to faces or features in the body. When the SurfaceBody has its IsSolid return True, this method sets the AppearanceSourceType to kBodyAppearance for all the features and kFeatureAppearance for all the faces in the body. When the SurfaceBody has its IsSolid return False, this method sets the AppearanceSourceType to kBodyAppearance for all the features directly owned by the work surface and kFeatureAppearance for all the faces in the body. |
| [Delete](../SurfaceBodyProxy/SurfaceBodyProxy_Delete.md) | Method that deletes this SurfaceBody object. |
| [FindUsingRay](../SurfaceBodyProxy/SurfaceBodyProxy_FindUsingRay.md) | Please note: As of Autodesk Inventor 5.3 Service Pack 2, the FindUsingRay method below has superseded LocateUsingRay. Please update your applications accordingly. Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. There is also a precedence in the type of entities returned. The entities returned can be Vertex, Edge, or Face objects. The precedence is in that order. If the ray intersects a vertex, then that vertex is returned and none of the edges or faces that connect to that vertex are returned. If the ray intersects an edge, then that edge is returned and none of the faces that connect to the edge are returned. If the ray intersects a face, then that face is returned. If desired, you can use the functionality provided by the B-Rep portion of the API to obtain the various associated objects from the entity returned. For example if you need a face but an edge is returned, you can use the Faces property of the Edge object to get the associated faces. The start point defines the physical starting point from which to determine intersections. Any intersections behind the start point are ignored. However, the ray is infinite from the start point, so all intersections in the direction of the ray will be returned. |
| [GetAppearanceTextureMappingData](../SurfaceBodyProxy/SurfaceBodyProxy_GetAppearanceTextureMappingData.md) | Gets the texture mapping type and alignment. |
| [GetExistingFacets](../SurfaceBodyProxy/SurfaceBodyProxy_GetExistingFacets.md) | Obtain the faceted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing/ |
| [GetExistingFacetsAndTextureMap](../SurfaceBodyProxy/SurfaceBodyProxy_GetExistingFacetsAndTextureMap.md) | Method that returns the specified set of existing display facets. Existing display facets are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateFacets method which will calculate new facets to a given tolerance at double-precision accuracy. |
| [GetExistingFacetTolerances](../SurfaceBodyProxy/SurfaceBodyProxy_GetExistingFacetTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method. |
| [GetExistingStrokes](../SurfaceBodyProxy/SurfaceBodyProxy_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../SurfaceBodyProxy/SurfaceBodyProxy_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetFaceColors](../SurfaceBodyProxy/SurfaceBodyProxy_GetFaceColors.md) | Method that gets the appearance colors for the faces. The returned ObjectCollection contains the Color objects with the same sequence as the corresponding Face objects in the input Faces argument. |
| [GetReferenceKey](../SurfaceBodyProxy/SurfaceBodyProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [IsEntityValid](../SurfaceBodyProxy/SurfaceBodyProxy_IsEntityValid.md) | Method that returns whether an entity passes the quality check at the specified level. |
| [LocateUsingPoint](../SurfaceBodyProxy/SurfaceBodyProxy_LocateUsingPoint.md) | Finds the object of specified type within the proximity of the given point. By default an internal tolerance is used to gauge the proximity. |
| [SetAppearanceTextureMappingData](../SurfaceBodyProxy/SurfaceBodyProxy_SetAppearanceTextureMappingData.md) | Method that sets the texture mapping type and alignment. Setting this value is only valid when the appearance assigned to the body has a texture defined. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedByFeatures](../SurfaceBodyProxy/SurfaceBodyProxy_AffectedByFeatures.md) | Property that returns the features that affected this body. The returned enumerator includes the feature that created this body. This property returns Nothing for transient bodies |
| [AlternateBody](../SurfaceBodyProxy/SurfaceBodyProxy_AlternateBody.md) | Property that returns a new SurfaceBody that was derived from the existing body using the specified form input. The primary purpose of this property is to obtain a body that consists entirely of NURBS surfaces. |
| [Appearance](../SurfaceBodyProxy/SurfaceBodyProxy_Appearance.md) | Gets and sets the current appearance of the body. |
| [AppearanceSourceType](../SurfaceBodyProxy/SurfaceBodyProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the body. |
| [Application](../SurfaceBodyProxy/SurfaceBodyProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SurfaceBodyProxy/SurfaceBodyProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ComponentDefinition](../SurfaceBodyProxy/SurfaceBodyProxy_ComponentDefinition.md) | Gets the primary that resides in this file. |
| [ConcaveEdges](../SurfaceBodyProxy/SurfaceBodyProxy_ConcaveEdges.md) | Property that returns an that contains all of the concave edges of the surface body. The CollectionType of the output EdgeCollection is set to kAllConcave. |
| [ContainingOccurrence](../SurfaceBodyProxy/SurfaceBodyProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ConvexEdges](../SurfaceBodyProxy/SurfaceBodyProxy_ConvexEdges.md) | Property that returns an that contains all of the convex edges of the surface body. The CollectionType of the output EdgeCollection is set to kAllConvex. |
| [CreatedByFeature](../SurfaceBodyProxy/SurfaceBodyProxy_CreatedByFeature.md) | Property that returns the feature that resulted in the creation of this body. This property returns Nothing for transient bodies. |
| [DataIO](../SurfaceBodyProxy/SurfaceBodyProxy_DataIO.md) | Returns the DataIO object. |
| [Edges](../SurfaceBodyProxy/SurfaceBodyProxy_Edges.md) | Gets the referenced by this SurfaceBody. |
| [Exported](../SurfaceBodyProxy/SurfaceBodyProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Faces](../SurfaceBodyProxy/SurfaceBodyProxy_Faces.md) | Property that returns a collection object generated as a result of the feature. |
| [FaceShells](../SurfaceBodyProxy/SurfaceBodyProxy_FaceShells.md) | Property that returns the collection object. |
| [GeometryForm](../SurfaceBodyProxy/SurfaceBodyProxy_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [IsPointInside](../SurfaceBodyProxy/SurfaceBodyProxy_IsPointInside.md) | Property that returns a constant indicating whether the specified point is inside, on or outside the body. |
| [IsSolid](../SurfaceBodyProxy/SurfaceBodyProxy_IsSolid.md) | Determine if this SurfaceBody is solid. |
| [IsTransient](../SurfaceBodyProxy/SurfaceBodyProxy_IsTransient.md) | Property that specified if this SurfaceBody is transient or not. |
| [MassProperties](../SurfaceBodyProxy/SurfaceBodyProxy_MassProperties.md) | Read-only property that returns mass properties for this body. |
| [Name](../SurfaceBodyProxy/SurfaceBodyProxy_Name.md) | Gets and sets the name of the body. |
| [NativeObject](../SurfaceBodyProxy/SurfaceBodyProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OrientedMinimumRangeBox](../SurfaceBodyProxy/SurfaceBodyProxy_OrientedMinimumRangeBox.md) | Retrieves the oriented minimum range box for this object. |
| [Parent](../SurfaceBodyProxy/SurfaceBodyProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PreciseRangeBox](../SurfaceBodyProxy/SurfaceBodyProxy_PreciseRangeBox.md) | Gets a tight fitting bounding box for this body. |
| [RangeBox](../SurfaceBodyProxy/SurfaceBodyProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../SurfaceBodyProxy/SurfaceBodyProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vertices](../SurfaceBodyProxy/SurfaceBodyProxy_Vertices.md) | Property that retrieves all vertices on the body. |
| [Visible](../SurfaceBodyProxy/SurfaceBodyProxy_Visible.md) | Gets and sets the visibility of the body. |
| [Volume](../SurfaceBodyProxy/SurfaceBodyProxy_Volume.md) | Property that returns the volume of the component in database units. |
| [Wires](../SurfaceBodyProxy/SurfaceBodyProxy_Wires.md) | Property returning the Wires collection object associated with this SurfaceBody. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |