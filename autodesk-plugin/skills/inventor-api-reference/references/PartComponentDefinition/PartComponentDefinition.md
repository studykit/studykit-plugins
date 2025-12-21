# PartComponentDefinition Object

Derived from: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) Object

## Description

The PartComponentDefinition object that provides access to the Part.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearAppearanceOverrides](../PartComponentDefinition/PartComponentDefinition_ClearAppearanceOverrides.md) | Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences. |
| [CreateFactory](../PartComponentDefinition/PartComponentDefinition_CreateFactory.md) | Converts a part to an iPart factory. |
| [CreateGeometryIntent](../PartComponentDefinition/PartComponentDefinition_CreateGeometryIntent.md) | Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating annotations in the model. They are used to identify geometry and optionally specific locations on that geometry. |
| [DeleteObjects](../PartComponentDefinition/PartComponentDefinition_DeleteObjects.md) | Method that deletes a collection of objects that belong to the part. |
| [ExportObjects](../PartComponentDefinition/PartComponentDefinition_ExportObjects.md) | Marks all the input objects as exported. |
| [FindUsingPoint](../PartComponentDefinition/PartComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingRay](../PartComponentDefinition/PartComponentDefinition_FindUsingRay.md) | Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. |
| [FindUsingVector](../PartComponentDefinition/PartComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetEndOfPartPosition](../PartComponentDefinition/PartComponentDefinition_GetEndOfPartPosition.md) | Gets the current end of part position in the browser (in parts). |
| [GetUnusedGeometries](../PartComponentDefinition/PartComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [PurgeUnusedGeometries](../PartComponentDefinition/PartComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../PartComponentDefinition/PartComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |
| [SetEndOfPartToTopOrBottom](../PartComponentDefinition/PartComponentDefinition_SetEndOfPartToTopOrBottom.md) | Method that positions the end-of-part marker at the top or bottom of the browser. |
| [SuppressFeatures](../PartComponentDefinition/PartComponentDefinition_SuppressFeatures.md) | Method that suppresses the specified features. |
| [UnsuppressFeatures](../PartComponentDefinition/PartComponentDefinition_UnsuppressFeatures.md) | Method that unsuppresses the specified features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnalysisManager](../PartComponentDefinition/PartComponentDefinition_AnalysisManager.md) | Property that returns the AnalysisManager object. |
| [AnnotationPlanes](../PartComponentDefinition/PartComponentDefinition_AnnotationPlanes.md) | Read-only property that returns the AnnotationPlanes collection object. This object provides access to all of the annotation planes in the part. |
| [AppearanceOverridesObjects](../PartComponentDefinition/PartComponentDefinition_AppearanceOverridesObjects.md) | Gets the objects that have appearance overrides in the active design view. The objects can include faces, features, work surfaces and surface bodies. |
| [Application](../PartComponentDefinition/PartComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PartComponentDefinition/PartComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BIMComponent](../PartComponentDefinition/PartComponentDefinition_BIMComponent.md) | Read-only property that returns the BIMComponent object associated with this component definition. |
| [BOMQuantity](../PartComponentDefinition/PartComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../PartComponentDefinition/PartComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../PartComponentDefinition/PartComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [CompactModelHistoryOnNextSave](../PartComponentDefinition/PartComponentDefinition_CompactModelHistoryOnNextSave.md) | Gets/Sets the flag that decides whether the BRep's modifications through its history are saved explicitly in the next save or not (independent of CompactModelHistory setting). |
| [DataIO](../PartComponentDefinition/PartComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [Document](../PartComponentDefinition/PartComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [FactoryDocument](../PartComponentDefinition/PartComponentDefinition_FactoryDocument.md) | Read-only property that returns the model state factory document when IsModelStateMember returns True. |
| [Features](../PartComponentDefinition/PartComponentDefinition_Features.md) | Property that returns the PartFeatures collection object. |
| [HasMultipleSolidBodies](../PartComponentDefinition/PartComponentDefinition_HasMultipleSolidBodies.md) | Determines whether the part contains multiple solid bodies or not. |
| [iMateDefinitions](../PartComponentDefinition/PartComponentDefinition_iMateDefinitions.md) | Property that returns the iMateDefinitions collection object associated with this part. |
| [iPartFactory](../PartComponentDefinition/PartComponentDefinition_iPartFactory.md) | Property that returns the iPartFactory object. This property will fail in the case where the part is not an iPart Factory. You can determine this by using the IsiPartFactory property. |
| [iPartMember](../PartComponentDefinition/PartComponentDefinition_iPartMember.md) | Property that returns the iPartMember object. |
| [IsContentMember](../PartComponentDefinition/PartComponentDefinition_IsContentMember.md) | Property that indicates if this part is a Content Center part or not. A value of True indicates it is a Content Center part. |
| [IsiPartFactory](../PartComponentDefinition/PartComponentDefinition_IsiPartFactory.md) | Property that returns if the part is an iPart Factory or not. It returns True in the case where the part is a factory. If True, the factory can be obtained using the iPartFactory property. |
| [IsiPartMember](../PartComponentDefinition/PartComponentDefinition_IsiPartMember.md) | Property that returns the iPartMember object. This property will fail in the case where the part is not an iPart Member. You can determine this by using the IsiPartMember property. |
| [IsModelStateFactory](../PartComponentDefinition/PartComponentDefinition_IsModelStateFactory.md) | Read-only property that returns whether the document is a model state factory document or not. |
| [IsModelStateMember](../PartComponentDefinition/PartComponentDefinition_IsModelStateMember.md) | Read-only property that returns whether the document is a model state member document or not. |
| [MassProperties](../PartComponentDefinition/PartComponentDefinition_MassProperties.md) | Mass properties for this ComponentDefinition. |
| [MeshFeatureSets](../PartComponentDefinition/PartComponentDefinition_MeshFeatureSets.md) | Read-only property that returns the MeshFeatureSets collection object. |
| [ModelAnnotations](../PartComponentDefinition/PartComponentDefinition_ModelAnnotations.md) | Read-only property that returns the ModelAnnotations collection object. This object provides access to all of the model annotations in the part. |
| [ModelGeometryVersion](../PartComponentDefinition/PartComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [ModelStates](../PartComponentDefinition/PartComponentDefinition_ModelStates.md) | Read-only property that returns the ModelStates object. |
| [ModelToleranceFeatures](../PartComponentDefinition/PartComponentDefinition_ModelToleranceFeatures.md) | Returns the ModelToleranceFeatures collection object. This object provides access to all of the model annotations in the part. |
| [Occurrences](../PartComponentDefinition/PartComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../PartComponentDefinition/PartComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [Parameters](../PartComponentDefinition/PartComponentDefinition_Parameters.md) | Gets the Parameters collection object that encapsulates all of the parameters defined in this ComponentDefinition. |
| [PartEvents](../PartComponentDefinition/PartComponentDefinition_PartEvents.md) | Property that returns the PartEvents source object. |
| [PointClouds](../PartComponentDefinition/PartComponentDefinition_PointClouds.md) | Gets the PointClouds collection object that encapsulates all of the point clouds defined in this Component Definition. |
| [PreciseRangeBox](../PartComponentDefinition/PartComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [RangeBox](../PartComponentDefinition/PartComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferenceComponents](../PartComponentDefinition/PartComponentDefinition_ReferenceComponents.md) | Property that returns the ReferenceComponents collection object. |
| [RepresentationsManager](../PartComponentDefinition/PartComponentDefinition_RepresentationsManager.md) | Read-only property that returns the RepresentationsManager object. |
| [RolledBackForEdit](../PartComponentDefinition/PartComponentDefinition_RolledBackForEdit.md) | Property that gets whether the model is currently rolled back to a previous point in the feature history. |
| [SketchBlockDefinitions](../PartComponentDefinition/PartComponentDefinition_SketchBlockDefinitions.md) | Property that returns the SketchBlockDefinitions collection object. |
| [Sketches](../PartComponentDefinition/PartComponentDefinition_Sketches.md) | Gets the PlanarSketches collection object that encapsulates all of the planar sketches defined in this ComponentDefinition. |
| [Sketches3D](../PartComponentDefinition/PartComponentDefinition_Sketches3D.md) | Property that returns the Sketches3D collection object that encapsulates all of the 3D sketches defined in this ComponentDefinition. |
| [SurfaceBodies](../PartComponentDefinition/PartComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Type](../PartComponentDefinition/PartComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserCoordinateSystems](../PartComponentDefinition/PartComponentDefinition_UserCoordinateSystems.md) | Property that returns the UserCoordinateSystems collection object. |
| [WorkAxes](../PartComponentDefinition/PartComponentDefinition_WorkAxes.md) | Property that returns the WorkAxes collection object. |
| [WorkPlanes](../PartComponentDefinition/PartComponentDefinition_WorkPlanes.md) | Property that returns the WorkPlanes collection object. |
| [WorkPoints](../PartComponentDefinition/PartComponentDefinition_WorkPoints.md) | Property that returns the WorkPoints collection object. |
| [WorkSurfaces](../PartComponentDefinition/PartComponentDefinition_WorkSurfaces.md) | Property that returns the collection object that encapsulates all of the work surfaces defined in this PartComponentDefinition. |

## Accessed From

[PartComponentDefinitions.Item](../PartComponentDefinitions/PartComponentDefinitions_Item.md), [PartDocument.ComponentDefinition](../PartDocument/PartDocument_ComponentDefinition.md)

## Derived Classes

[SheetMetalComponentDefinition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Part SimplifyFeature Sample](../../sample-programs/PartSimplifyFeatureSample_Sample.md) | This sample demonstrates how to create a simplify feature in part document. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 4
