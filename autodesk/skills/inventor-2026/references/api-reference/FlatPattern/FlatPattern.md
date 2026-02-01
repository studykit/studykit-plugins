# FlatPattern Object

Derived from: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) Object

## Description

The FlatPattern object represents the unfolded model in a sheet metal document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateGeometryIntent](../FlatPattern/FlatPattern_CreateGeometryIntent.md) | Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating annotations in the model. They are used to identify geometry and optionally specific locations on that geometry. |
| [Delete](../FlatPattern/FlatPattern_Delete.md) | Method that deletes the FlatPattern. |
| [DeleteObjects](../FlatPattern/FlatPattern_DeleteObjects.md) | Method that deletes a collection of objects that belong to the flat pattern. |
| [Edit](../FlatPattern/FlatPattern_Edit.md) | Method that puts the FlatPattern in edit mode. |
| [ExitEdit](../FlatPattern/FlatPattern_ExitEdit.md) | Method that causes the FlatPattern editing environment to be closed and the user interface to return to sheet metal editing environment. |
| [FindUsingPoint](../FlatPattern/FlatPattern_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingRay](../FlatPattern/FlatPattern_FindUsingRay.md) | Method that fires a ray through the flat pattern and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. |
| [FindUsingVector](../FlatPattern/FlatPattern_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetEdgesOfType](../FlatPattern/FlatPattern_GetEdgesOfType.md) | Method that returns edges of the specified type from the flat pattern body. |
| [GetEndOfPartPosition](../FlatPattern/FlatPattern_GetEndOfPartPosition.md) | Method that returns the current end of part position in the browser in parts and assemblies. |
| [GetFlatPatternEntity](../FlatPattern/FlatPattern_GetFlatPatternEntity.md) | Method that returns the corresponding BRep entity (face, edge, etc.) in the flat pattern body given a BRep entity in the sheet metal body. |
| [GetSheetMetalEntity](../FlatPattern/FlatPattern_GetSheetMetalEntity.md) | Returns the corresponding BRep entity (face, edge, etc.) in the sheet metal body given a BRep entity in the flat pattern body. If an entity is not found, the method returns Nothing. If multiple matches are found, an ObjectsEnumerator is returned. |
| [GetUnusedGeometries](../FlatPattern/FlatPattern_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [PurgeUnusedGeometries](../FlatPattern/FlatPattern_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../FlatPattern/FlatPattern_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |
| [SetEndOfPartToTopOrBottom](../FlatPattern/FlatPattern_SetEndOfPartToTopOrBottom.md) | Inventor::PartComponentDefinition::SetEndOfPartToTopOrBottom |
| [SuppressFeatures](../FlatPattern/FlatPattern_SuppressFeatures.md) | Method that suppresses the specified features. This is limited to the features created in the flat pattern. |
| [UnsuppressFeatures](../FlatPattern/FlatPattern_UnsuppressFeatures.md) | Method that unsuppresses the specified features. This is limited to the features created in the flat pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlanes](../FlatPattern/FlatPattern_AnnotationPlanes.md) | Read-only property that returns the AnnotationPlanes collection object. This object provides access to all of the annotation planes in the part. |
| [Application](../FlatPattern/FlatPattern_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ASideFace](../FlatPattern/FlatPattern_ASideFace.md) | Read-only property that returns the ASideFaceDefinition from the folded model that was used to create the flat pattern. |
| [AttributeSets](../FlatPattern/FlatPattern_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BaseFace](../FlatPattern/FlatPattern_BaseFace.md) | Property that returns the base face from the folded model that was used to create the flat pattern. |
| [BendAngleReportType](../FlatPattern/FlatPattern_BendAngleReportType.md) | Gets and sets which angle is reported in the flat pattern. |
| [Body](../FlatPattern/FlatPattern_Body.md) | Property that returns the corresponding SurfaceBody. |
| [BOMQuantity](../FlatPattern/FlatPattern_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../FlatPattern/FlatPattern_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [BottomFace](../FlatPattern/FlatPattern_BottomFace.md) | Property that returns the bottom face of the flat pattern. |
| [ClientGraphicsCollection](../FlatPattern/FlatPattern_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [DataIO](../FlatPattern/FlatPattern_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [Document](../FlatPattern/FlatPattern_Document.md) | Property that returns the containing Document object. |
| [Features](../FlatPattern/FlatPattern_Features.md) | Property that returns the collection object that provides access to the features associated with the flat pattern. |
| [FlatBendResults](../FlatPattern/FlatPattern_FlatBendResults.md) | Property that returns the FlatBendResults collection object that contains information about all the bends in the flat pattern. |
| [FlatPatternOrientations](../FlatPattern/FlatPattern_FlatPatternOrientations.md) | Gets the FlatPatternOrientations collection object. |
| [FlatPunchResults](../FlatPattern/FlatPattern_FlatPunchResults.md) | Property that returns the FlatPunchResults collection object that contains information about all the punches in the flat pattern. |
| [GraphicsDataSetsCollection](../FlatPattern/FlatPattern_GraphicsDataSetsCollection.md) | Inventor::ComponentDefinition::GraphicsDataSetsCollection |
| [IgnorePunchToolFeaturesRepresentationOverrides](../FlatPattern/FlatPattern_IgnorePunchToolFeaturesRepresentationOverrides.md) | Gets and sets whether to ignore the punch tool features representation overrides in flat pattern. |
| [Length](../FlatPattern/FlatPattern_Length.md) | Property that returns the length of the flat pattern. |
| [MassProperties](../FlatPattern/FlatPattern_MassProperties.md) | Property that returns the MassProperties object for the flat pattern. |
| [ModelAnnotations](../FlatPattern/FlatPattern_ModelAnnotations.md) | Read-only property that returns the ModelAnnotations collection object. This object provides access to all of the model annotations in the part. |
| [ModelGeometryVersion](../FlatPattern/FlatPattern_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [ModelToleranceFeatures](../FlatPattern/FlatPattern_ModelToleranceFeatures.md) | Returns the ModelToleranceFeatures collection object. This object provides access to all of the model annotations in the part. |
| [Occurrences](../FlatPattern/FlatPattern_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../FlatPattern/FlatPattern_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [Parameters](../FlatPattern/FlatPattern_Parameters.md) | Property that returns the set of parameters for the flat pattern. |
| [Parent](../FlatPattern/FlatPattern_Parent.md) | Property that returns the parent SheetMetalComponentDefinition object. |
| [PartEvents](../FlatPattern/FlatPattern_PartEvents.md) | Property that returns the PartEvents object associated with the flat pattern. This object will fire events for changes that occur to the flat pattern. |
| [PreciseRangeBox](../FlatPattern/FlatPattern_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [PunchRepresentationType](../FlatPattern/FlatPattern_PunchRepresentationType.md) | Gets and sets the punch representation to use for the flat pattern. |
| [RangeBox](../FlatPattern/FlatPattern_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RepresentationsManager](../FlatPattern/FlatPattern_RepresentationsManager.md) | Read-only property that returns the RepresentationsManager object. |
| [RolledBackForEdit](../FlatPattern/FlatPattern_RolledBackForEdit.md) | Property that gets whether the flat pattern model is currently rolled back to a previous point in the feature history. |
| [SketchBlockDefinitions](../FlatPattern/FlatPattern_SketchBlockDefinitions.md) | Inventor::PartComponentDefinition::SketchBlockDefinitions |
| [Sketches](../FlatPattern/FlatPattern_Sketches.md) | Inventor::PartComponentDefinition::Sketches |
| [Sketches3D](../FlatPattern/FlatPattern_Sketches3D.md) | Inventor::PartComponentDefinition::Sketchs3D |
| [SurfaceBodies](../FlatPattern/FlatPattern_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [TopFace](../FlatPattern/FlatPattern_TopFace.md) | Property that returns top face of the flat pattern. |
| [Type](../FlatPattern/FlatPattern_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserCoordinateSystems](../FlatPattern/FlatPattern_UserCoordinateSystems.md) | Property that returns the UserCoordinateSystems collection object. |
| [Width](../FlatPattern/FlatPattern_Width.md) | Property that returns the width of the flat pattern. |
| [WorkAxes](../FlatPattern/FlatPattern_WorkAxes.md) | Property that returns that collection object that provides access to all of the existing work axis objects in the flat pattern and provides the functionality to create new work axis objects. |
| [WorkPlanes](../FlatPattern/FlatPattern_WorkPlanes.md) | Property that returns that collection object that provides access to all of the existing work plane objects in the flat pattern and provides the functionality to create new work plane objects. |
| [WorkPoints](../FlatPattern/FlatPattern_WorkPoints.md) | Property that returns that collection object that provides access to all of the existing work point objects in the flat pattern and provides the functionality to create new work point objects. |

## Accessed From

[FlatBendResult.Parent](../FlatBendResult/FlatBendResult_Parent.md), [FlatPatternOrientation.Parent](../FlatPatternOrientation/FlatPatternOrientation_Parent.md), [FlatPatternPlate.Parent](FlatPatternPlate_Parent.md), [FlatPunchResult.Parent](../FlatPunchResult/FlatPunchResult_Parent.md), [SheetMetalComponentDefinition.FlatPattern](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FlatPattern.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Publish FlatPattern to STEP](../../sample-programs/ExportFlatPatternToSTEP_Sample.md) | This sample demonstrates how to save a FlatPattern file using the STEP translator add-in. |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |
| [Publish FlatPattern to DXF](../../sample-programs/PublishFlatPatternToDXF_Sample.md) | This sample demonstrates how to save a FlatPattern file using the DXF translator add-in. |

## Version

Introduced in version 6
