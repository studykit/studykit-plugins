# SurfaceBody Object

## Description

The SurfaceBody object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BindTransientKeyToObject](../SurfaceBody/SurfaceBody_BindTransientKeyToObject.md) | Bind the transient key of a subentity on this body to a live object. |
| [CalculateFacets](../SurfaceBody/SurfaceBody_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsAndTextureMap](../SurfaceBody/SurfaceBody_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsWithOptions](../SurfaceBody/SurfaceBody_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../SurfaceBody/SurfaceBody_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree. |
| [CalculateStrokesWithOptions](../SurfaceBody/SurfaceBody_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [ClearAppearanceOverrides](../SurfaceBody/SurfaceBody_ClearAppearanceOverrides.md) | Method that clears all the appearance overrides that have been applied to faces or features in the body. When the SurfaceBody has its IsSolid return True, this method sets the AppearanceSourceType to kBodyAppearance for all the features and kFeatureAppearance for all the faces in the body. When the SurfaceBody has its IsSolid return False, this method sets the AppearanceSourceType to kBodyAppearance for all the features directly owned by the work surface and kFeatureAppearance for all the faces in the body. |
| [Delete](../SurfaceBody/SurfaceBody_Delete.md) | Method that deletes this SurfaceBody object. |
| [FindUsingRay](../SurfaceBody/SurfaceBody_FindUsingRay.md) | Please note: As of Autodesk Inventor 5.3 Service Pack 2, the FindUsingRay method below has superseded LocateUsingRay. Please update your applications accordingly. Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. There is also a precedence in the type of entities returned. The entities returned can be Vertex, Edge, or Face objects. The precedence is in that order. If the ray intersects a vertex, then that vertex is returned and none of the edges or faces that connect to that vertex are returned. If the ray intersects an edge, then that edge is returned and none of the faces that connect to the edge are returned. If the ray intersects a face, then that face is returned. If desired, you can use the functionality provided by the B-Rep portion of the API to obtain the various associated objects from the entity returned. For example if you need a face but an edge is returned, you can use the Faces property of the Edge object to get the associated faces. The start point defines the physical starting point from which to determine intersections. Any intersections behind the start point are ignored. However, the ray is infinite from the start point, so all intersections in the direction of the ray will be returned. |
| [GetAppearanceTextureMappingData](../SurfaceBody/SurfaceBody_GetAppearanceTextureMappingData.md) | Gets the texture mapping type and alignment. |
| [GetExistingFacets](../SurfaceBody/SurfaceBody_GetExistingFacets.md) | Obtain the faceted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing/ |
| [GetExistingFacetsAndTextureMap](../SurfaceBody/SurfaceBody_GetExistingFacetsAndTextureMap.md) | Method that returns the specified set of existing display facets. Existing display facets are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateFacets method which will calculate new facets to a given tolerance at double-precision accuracy. |
| [GetExistingFacetTolerances](../SurfaceBody/SurfaceBody_GetExistingFacetTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method. |
| [GetExistingStrokes](../SurfaceBody/SurfaceBody_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../SurfaceBody/SurfaceBody_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetFaceColors](../SurfaceBody/SurfaceBody_GetFaceColors.md) | Method that gets the appearance colors for the faces. The returned ObjectCollection contains the Color objects with the same sequence as the corresponding Face objects in the input Faces argument. |
| [GetReferenceKey](../SurfaceBody/SurfaceBody_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [IsEntityValid](../SurfaceBody/SurfaceBody_IsEntityValid.md) | Method that returns whether an entity passes the quality check at the specified level. |
| [LocateUsingPoint](../SurfaceBody/SurfaceBody_LocateUsingPoint.md) | Finds the object of specified type within the proximity of the given point. By default an internal tolerance is used to gauge the proximity. |
| [SetAppearanceTextureMappingData](../SurfaceBody/SurfaceBody_SetAppearanceTextureMappingData.md) | Method that sets the texture mapping type and alignment. Setting this value is only valid when the appearance assigned to the body has a texture defined. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedByFeatures](../SurfaceBody/SurfaceBody_AffectedByFeatures.md) | Property that returns the features that affected this body. The returned enumerator includes the feature that created this body. This property returns Nothing for transient bodies |
| [AlternateBody](../SurfaceBody/SurfaceBody_AlternateBody.md) | Property that returns a new SurfaceBody that was derived from the existing body using the specified form input. The primary purpose of this property is to obtain a body that consists entirely of NURBS surfaces. |
| [Appearance](../SurfaceBody/SurfaceBody_Appearance.md) | Gets and sets the current appearance of the body. |
| [AppearanceSourceType](../SurfaceBody/SurfaceBody_AppearanceSourceType.md) | Gets and sets the source of the appearance for the body. |
| [Application](../SurfaceBody/SurfaceBody_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SurfaceBody/SurfaceBody_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ComponentDefinition](../SurfaceBody/SurfaceBody_ComponentDefinition.md) | Gets the primary that resides in this file. |
| [ConcaveEdges](../SurfaceBody/SurfaceBody_ConcaveEdges.md) | Property that returns an that contains all of the concave edges of the surface body. The CollectionType of the output EdgeCollection is set to kAllConcave. |
| [ConvexEdges](../SurfaceBody/SurfaceBody_ConvexEdges.md) | Property that returns an that contains all of the convex edges of the surface body. The CollectionType of the output EdgeCollection is set to kAllConvex. |
| [CreatedByFeature](../SurfaceBody/SurfaceBody_CreatedByFeature.md) | Property that returns the feature that resulted in the creation of this body. This property returns Nothing for transient bodies. |
| [DataIO](../SurfaceBody/SurfaceBody_DataIO.md) | Returns the DataIO object. |
| [Edges](../SurfaceBody/SurfaceBody_Edges.md) | Gets the referenced by this SurfaceBody. |
| [Exported](../SurfaceBody/SurfaceBody_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Faces](../SurfaceBody/SurfaceBody_Faces.md) | Property that returns a collection object generated as a result of the feature. |
| [FaceShells](../SurfaceBody/SurfaceBody_FaceShells.md) | Property that returns the collection object. |
| [GeometryForm](../SurfaceBody/SurfaceBody_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [IsPointInside](../SurfaceBody/SurfaceBody_IsPointInside.md) | Property that returns a constant indicating whether the specified point is inside, on or outside the body. |
| [IsSolid](../SurfaceBody/SurfaceBody_IsSolid.md) | Determine if this SurfaceBody is solid. |
| [IsTransient](../SurfaceBody/SurfaceBody_IsTransient.md) | Property that specified if this SurfaceBody is transient or not. |
| [MassProperties](../SurfaceBody/SurfaceBody_MassProperties.md) | Read-only property that returns mass properties for this body. |
| [Name](../SurfaceBody/SurfaceBody_Name.md) | Gets and sets the name of the body. |
| [OrientedMinimumRangeBox](../SurfaceBody/SurfaceBody_OrientedMinimumRangeBox.md) | Retrieves the oriented minimum range box for this object. |
| [Parent](../SurfaceBody/SurfaceBody_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PreciseRangeBox](../SurfaceBody/SurfaceBody_PreciseRangeBox.md) | Gets a tight fitting bounding box for this body. |
| [RangeBox](../SurfaceBody/SurfaceBody_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../SurfaceBody/SurfaceBody_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Vertices](../SurfaceBody/SurfaceBody_Vertices.md) | Property that retrieves all vertices on the body. |
| [Visible](../SurfaceBody/SurfaceBody_Visible.md) | Gets and sets the visibility of the body. |
| [Volume](../SurfaceBody/SurfaceBody_Volume.md) | Property that returns the volume of the component in database units. |
| [Wires](../SurfaceBody/SurfaceBody_Wires.md) | Property returning the Wires collection object associated with this SurfaceBody. |

## Accessed From

[ApplicationUtilities.CreateHolePatch2](ApplicationUtilities_CreateHolePatch2.md), [ApplicationUtilities.CreateHolePatch3](ApplicationUtilities_CreateHolePatch3.md), [ComponentGraphics.Body](../ComponentGraphics/ComponentGraphics_Body.md), [CoreCavityDefinition.PartBody](CoreCavityDefinition_PartBody.md), [CoreCavityDefinition.WorkpieceBody](CoreCavityDefinition_WorkpieceBody.md), [CoreCavityFeature.Cavity](CoreCavityFeature_Cavity.md), [CoreCavityFeature.Core](CoreCavityFeature_Core.md), [CoreCavityFeatureProxy.Cavity](CoreCavityFeatureProxy_Cavity.md), [CoreCavityFeatureProxy.Core](CoreCavityFeatureProxy_Core.md), [Edge.Parent](../Edge/Edge_Parent.md), [EdgeLoop.Parent](../EdgeLoop/EdgeLoop_Parent.md), [EdgeLoopProxy.Parent](../EdgeLoopProxy/EdgeLoopProxy_Parent.md), [EdgeProxy.Parent](../EdgeProxy/EdgeProxy_Parent.md), [EdgeUse.Parent](../EdgeUse/EdgeUse_Parent.md), [EdgeUseProxy.Parent](../EdgeUseProxy/EdgeUseProxy_Parent.md), [Face.AlternateBody](../Face/Face_AlternateBody.md), [Face.Parent](../Face/Face_Parent.md), [Face.SurfaceBody](../Face/Face_SurfaceBody.md), [FaceProxy.AlternateBody](../FaceProxy/FaceProxy_AlternateBody.md), [FaceProxy.Parent](../FaceProxy/FaceProxy_Parent.md), [FaceProxy.SurfaceBody](../FaceProxy/FaceProxy_SurfaceBody.md), [FaceShell.Parent](../FaceShell/FaceShell_Parent.md), [FaceShell.SurfaceBody](../FaceShell/FaceShell_SurfaceBody.md), [FaceShellProxy.Parent](../FaceShellProxy/FaceShellProxy_Parent.md), [FaceShellProxy.SurfaceBody](../FaceShellProxy/FaceShellProxy_SurfaceBody.md), [FlatPattern.Body](../FlatPattern/FlatPattern_Body.md), [InterferenceResult.InterferenceBody](../InterferenceResult/InterferenceResult_InterferenceBody.md), [MoldDefinition.Cavity](MoldDefinition_Cavity.md), [MoldDefinition.Core](MoldDefinition_Core.md), [MoldDefinition.PartBody](MoldDefinition_PartBody.md), [MoldDefinition.WorkpieceBody](MoldDefinition_WorkpieceBody.md), [RibDefinition.AffectedBody](../RibDefinition/RibDefinition_AffectedBody.md), [RunoffSurfaceDefinition.CreateRunoff](RunoffSurfaceDefinition_CreateRunoff.md), [RunoffSurfaceDefinition.CreateSingleRunoffPiece](RunoffSurfaceDefinition_CreateSingleRunoffPiece.md), [SilhouetteCurve.Body](../SilhouetteCurve/SilhouetteCurve_Body.md), [SilhouetteCurveProxy.Body](../SilhouetteCurveProxy/SilhouetteCurveProxy_Body.md), [SolidSweepDefinition.ToolBody](../SolidSweepDefinition/SolidSweepDefinition_ToolBody.md), [SurfaceBodies.Item](../SurfaceBodies/SurfaceBodies_Item.md), [SurfaceBody.AlternateBody](../SurfaceBody/SurfaceBody_AlternateBody.md), [SurfaceBodyDefinition.CreateTransientSurfaceBody](../SurfaceBodyDefinition/SurfaceBodyDefinition_CreateTransientSurfaceBody.md), [SurfaceBodyMassProperties.Parent](../SurfaceBodyMassProperties/SurfaceBodyMassProperties_Parent.md), [SurfaceBodyProxy.AlternateBody](../SurfaceBodyProxy/SurfaceBodyProxy_AlternateBody.md), [SurfaceBodyProxy.NativeObject](../SurfaceBodyProxy/SurfaceBodyProxy_NativeObject.md), [SurfaceGraphics.Body](../SurfaceGraphics/SurfaceGraphics_Body.md), [ToNextExtent.Terminator](../ToNextExtent/ToNextExtent_Terminator.md), [TransientBRep.Copy](../TransientBRep/TransientBRep_Copy.md), [TransientBRep.CreateIntersectionWithPlane](../TransientBRep/TransientBRep_CreateIntersectionWithPlane.md), [TransientBRep.CreateRuledSurface](../TransientBRep/TransientBRep_CreateRuledSurface.md), [TransientBRep.CreateSilhouetteCurve](../TransientBRep/TransientBRep_CreateSilhouetteCurve.md), [TransientBRep.CreateSolidBlock](../TransientBRep/TransientBRep_CreateSolidBlock.md), [TransientBRep.CreateSolidCylinderCone](../TransientBRep/TransientBRep_CreateSolidCylinderCone.md), [TransientBRep.CreateSolidSphere](../TransientBRep/TransientBRep_CreateSolidSphere.md), [TransientBRep.CreateSolidTorus](../TransientBRep/TransientBRep_CreateSolidTorus.md), [TransientBRep.ImprintBodies](../TransientBRep/TransientBRep_ImprintBodies.md), [Vertex.Parent](../Vertex/Vertex_Parent.md), [VertexProxy.Parent](../VertexProxy/VertexProxy_Parent.md), [Wire.Parent](../Wire/Wire_Parent.md)

## Derived Classes

[SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |

## Version

Introduced in version 4
