# SheetMetalComponentDefinition Object

Derived from: [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md) Object

## Description

The SheetMetalComponentDefinition object derives from the PartComponentDefinition object. It adds the sheet metal-specific behavior to the PartComponentDefinition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearAppearanceOverrides](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ClearAppearanceOverrides.md) | Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences. |
| [CreateFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CreateFactory.md) | Converts a part to an iPart factory. |
| [CreateGeometryIntent](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CreateGeometryIntent.md) | Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating annotations in the model. They are used to identify geometry and optionally specific locations on that geometry. |
| [DeleteObjects](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_DeleteObjects.md) | Method that deletes a collection of objects that belong to the part. |
| [ExportObjects](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ExportObjects.md) | Marks all the input objects as exported. |
| [FindUsingPoint](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingRay](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FindUsingRay.md) | Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. |
| [FindUsingVector](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetBodySheetMetalStyle](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_GetBodySheetMetalStyle.md) | Method that gets the sheet metal style for a surface body. |
| [GetEndOfPartPosition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_GetEndOfPartPosition.md) | Gets the current end of part position in the browser (in parts). |
| [GetUnusedGeometries](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [PurgeUnusedGeometries](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |
| [SetBodySheetMetalStyle](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SetBodySheetMetalStyle.md) | Method that sets the sheet metal style for a surface body. |
| [SetBodySheetMetalStyle2](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SetBodySheetMetalStyle2.md) | Method that sets the sheet metal style for a surface body, can ignore computation errors. |
| [SetEndOfPartToTopOrBottom](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SetEndOfPartToTopOrBottom.md) | Method that positions the end-of-part marker at the top or bottom of the browser. |
| [SuppressFeatures](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SuppressFeatures.md) | Method that suppresses the specified features. |
| [Unfold](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Unfold.md) | Method that generates the flat pattern. |
| [Unfold2](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Unfold2.md) | Method that generates the flat pattern with the input face as the base face. |
| [UnsuppressFeatures](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UnsuppressFeatures.md) | Method that unsuppresses the specified features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveSheetMetalStyle](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ActiveSheetMetalStyle.md) | Property that returns the active SheetMetalStyle object. |
| [AnalysisManager](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_AnalysisManager.md) | Property that returns the AnalysisManager object. |
| [AnnotationPlanes](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_AnnotationPlanes.md) | Read-only property that returns the AnnotationPlanes collection object. This object provides access to all of the annotation planes in the part. |
| [AppearanceOverridesObjects](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_AppearanceOverridesObjects.md) | Gets the objects that have appearance overrides in the active design view. The objects can include faces, features, work surfaces and surface bodies. |
| [Application](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ASideDefinitions](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ASideDefinitions.md) | Read-only property that returns the ASideFaceDefinitions collection object. |
| [AttributeSets](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendRadius](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BendRadius.md) | Property that returns the parameter that controls the bend radius of the part. |
| [BendReliefDepth](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BendReliefDepth.md) | Property that returns the parameter that controls the bend relief depth of the part. |
| [BendReliefWidth](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BendReliefWidth.md) | Property that returns the parameter that controls the bend relief width of the part. |
| [Bends](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Bends.md) | Inventor::PartComponentDefinition::Bends |
| [BIMComponent](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BIMComponent.md) | Read-only property that returns the BIMComponent object associated with this component definition. |
| [BOMQuantity](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [CompactModelHistoryOnNextSave](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CompactModelHistoryOnNextSave.md) | Gets/Sets the flag that decides whether the BRep's modifications through its history are saved explicitly in the next save or not (independent of CompactModelHistory setting). |
| [CornerReliefSize](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CornerReliefSize.md) | Property that returns the parameter that controls the corner relief size of the part. |
| [DataIO](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [Document](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [FactoryDocument](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FactoryDocument.md) | Read-only property that returns the model state factory document when IsModelStateMember returns True. |
| [Features](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Features.md) | Property that returns the PartFeatures collection object. |
| [FlatPattern](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FlatPattern.md) | Property that returns the FlatPattern object. If the sheet metal part hasn't been unfolded, this property returns Nothing. |
| [GapSize](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_GapSize.md) | Inventor::PartComponentDefinition::GapSize |
| [HasFlatPattern](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_HasFlatPattern.md) | Property that returns whether the sheet metal body has been unfolded and a FlatPattern object exists. |
| [HasMultipleSolidBodies](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_HasMultipleSolidBodies.md) | Determines whether the part contains multiple solid bodies or not. |
| [iMateDefinitions](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iMateDefinitions.md) | Property that returns the iMateDefinitions collection object associated with this part. |
| [iPartFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iPartFactory.md) | Property that returns the iPartFactory object. This property will fail in the case where the part is not an iPart Factory. You can determine this by using the IsiPartFactory property. |
| [iPartMember](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iPartMember.md) | Property that returns the iPartMember object. |
| [IsContentMember](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_IsContentMember.md) | Property that indicates if this part is a Content Center part or not. A value of True indicates it is a Content Center part. |
| [IsiPartFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_IsiPartFactory.md) | Property that returns if the part is an iPart Factory or not. It returns True in the case where the part is a factory. If True, the factory can be obtained using the iPartFactory property. |
| [IsiPartMember](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_IsiPartMember.md) | Property that returns the iPartMember object. This property will fail in the case where the part is not an iPart Member. You can determine this by using the IsiPartMember property. |
| [IsModelStateFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_IsModelStateFactory.md) | Read-only property that returns whether the document is a model state factory document or not. |
| [IsModelStateMember](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_IsModelStateMember.md) | Read-only property that returns whether the document is a model state member document or not. |
| [JacobiRadiusSize](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_JacobiRadiusSize.md) | Property that returns the parameter that controls the Jacobi radius size of the part. |
| [MassProperties](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_MassProperties.md) | Mass properties for this ComponentDefinition. |
| [MeshFeatureSets](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_MeshFeatureSets.md) | Read-only property that returns the MeshFeatureSets collection object. |
| [MinimumRemnant](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_MinimumRemnant.md) | Property that returns the parameter that controls the minimum remnant of the part. |
| [ModelAnnotations](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelAnnotations.md) | Read-only property that returns the ModelAnnotations collection object. This object provides access to all of the model annotations in the part. |
| [ModelGeometryVersion](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [ModelStates](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelStates.md) | Read-only property that returns the ModelStates object. |
| [ModelToleranceFeatures](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelToleranceFeatures.md) | Returns the ModelToleranceFeatures collection object. This object provides access to all of the model annotations in the part. |
| [Occurrences](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [Parameters](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Parameters.md) | Gets the Parameters collection object that encapsulates all of the parameters defined in this ComponentDefinition. |
| [PartEvents](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_PartEvents.md) | Property that returns the PartEvents source object. |
| [PointClouds](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_PointClouds.md) | Gets the PointClouds collection object that encapsulates all of the point clouds defined in this Component Definition. |
| [PreciseRangeBox](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [RangeBox](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferenceComponents](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ReferenceComponents.md) | Property that returns the ReferenceComponents collection object. |
| [RepresentationsManager](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_RepresentationsManager.md) | Read-only property that returns the RepresentationsManager object. |
| [RolledBackForEdit](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_RolledBackForEdit.md) | Property that gets whether the model is currently rolled back to a previous point in the feature history. |
| [SheetMetalStyles](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SheetMetalStyles.md) | Property that returns the SheetMetalStyles collection object. |
| [SketchBlockDefinitions](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SketchBlockDefinitions.md) | Property that returns the SketchBlockDefinitions collection object. |
| [Sketches](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Sketches.md) | Gets the PlanarSketches collection object that encapsulates all of the planar sketches defined in this ComponentDefinition. |
| [Sketches3D](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Sketches3D.md) | Property that returns the Sketches3D collection object that encapsulates all of the 3D sketches defined in this ComponentDefinition. |
| [SurfaceBodies](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Thickness](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Thickness.md) | Property that returns the parameter that controls the thickness of the part. |
| [TransitionRadius](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_TransitionRadius.md) | Property that returns the parameter that controls the transition radius of the part. |
| [Type](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UnfoldMethod.md) | Read-write property that gets and sets the currently active unfold method for the document. |
| [UnfoldMethods](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UnfoldMethods.md) | Property that returns the UnfoldMethods collection object. |
| [UserCoordinateSystems](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UserCoordinateSystems.md) | Property that returns the UserCoordinateSystems collection object. |
| [UseSheetMetalStyleMaterial](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UseSheetMetalStyleMaterial.md) | Read-write property that specifies if the material is defined by the sheet metal style or it is explictly set. |
| [UseSheetMetalStyleThickness](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UseSheetMetalStyleThickness.md) | Read-write property that specifies if the active thickness is defined by the sheet metal style or it is explictly set. |
| [UseSheetMetalStyleUnfoldMethod](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UseSheetMetalStyleUnfoldMethod.md) | Read-write property that specifies whether to use the unfold method specified by the sheet metal style or not. |
| [WorkAxes](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkAxes.md) | Property that returns the WorkAxes collection object. |
| [WorkPlanes](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkPlanes.md) | Property that returns the WorkPlanes collection object. |
| [WorkPoints](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkPoints.md) | Property that returns the WorkPoints collection object. |
| [WorkSurfaces](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkSurfaces.md) | Property that returns the collection object that encapsulates all of the work surfaces defined in this PartComponentDefinition. |

## Accessed From

[ASideDefinition.Parent](../ASideDefinition/ASideDefinition_Parent.md), [ASideDefinitions.Parent](../ASideDefinitions/ASideDefinitions_Parent.md), [Bend.Parent](../Bend/Bend_Parent.md), [FlatPattern.Parent](../FlatPattern/FlatPattern_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Report on punch feature ID's](../../sample-programs/PunchToolFeatureIDs_Sample.md) | This program demonstrates accessing punch features and creates a report of the punch ID's used. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Sheet Metal Style Display](../../sample-programs/SheetMetalStyle_Sample.md) | This sample illustrates getting information about sheet metal styles. |
| [Sheet Metal Thickness Editing](../../sample-programs/SheetMetalStyle_Thickness_Sample.md) | This sample illustrates editing the thickness of a sheet metal part. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |