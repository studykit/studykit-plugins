# AssemblyComponentDefinition Object

Derived from: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) Object

## Description

The AssemblyComponentDefinition object provides access to all of the assembly information of an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AdjustProxyContext](../AssemblyComponentDefinition/AssemblyComponentDefinition_AdjustProxyContext.md) | Returns the specified object proxy scoped into this assembly, trimming any portion of the context from any assembly in which this assembly is a subassembly. In other words, for the given object proxy, this method makes a new object proxy which has this component definition as the context definition. |
| [AnalyzeInterference](../AssemblyComponentDefinition/AssemblyComponentDefinition_AnalyzeInterference.md) | Method that analyzes the interference between two components. The input ObjectCollections contain the component occurrences that are to be checked for interference. If only one set is provided then interference checking is performed between all occurrences provided in the set. If two sets are provided then the overlap between the components of the two collections are calculated. |
| [ClearAppearanceOverrides](../AssemblyComponentDefinition/AssemblyComponentDefinition_ClearAppearanceOverrides.md) | Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences. |
| [CreateFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateFactory.md) | Method that converts an assembly to an iAssemblyFactory. The newly created iAssemblyFactory object will have an empty excel spreadsheet. |
| [CreateGeometryIntent](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateGeometryIntent.md) | Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating assembly joints. They are used to identify geometry and specific locations on that geometry. |
| [CreateVisibleOccurrenceFinder](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateVisibleOccurrenceFinder.md) | Method that creates an occurrence finder object that allows you to find all occurrences that are visible or hidden by a defined amount. By default, visible is defined by a portion of the part being visible from any view of the part. Optionally you can specify a camera to limit the viewing angle and the extents. |
| [ExportObjects](../AssemblyComponentDefinition/AssemblyComponentDefinition_ExportObjects.md) | Method that marks all the input objects as exported. |
| [FindUsingPoint](../AssemblyComponentDefinition/AssemblyComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingRay](../AssemblyComponentDefinition/AssemblyComponentDefinition_FindUsingRay.md) | Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. |
| [FindUsingVector](../AssemblyComponentDefinition/AssemblyComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetEndOfFeaturesPosition](../AssemblyComponentDefinition/AssemblyComponentDefinition_GetEndOfFeaturesPosition.md) | Gets the current end of Features position in the browser in an assembly. |
| [GetUnusedGeometries](../AssemblyComponentDefinition/AssemblyComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [HideAllRelationships](../AssemblyComponentDefinition/AssemblyComponentDefinition_HideAllRelationships.md) | Method that hides all of the assembly constraints, joints and iMate objects in the document. |
| [PurgeUnusedGeometries](../AssemblyComponentDefinition/AssemblyComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../AssemblyComponentDefinition/AssemblyComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |
| [SetEndOfFeaturesToTopOrBottom](../AssemblyComponentDefinition/AssemblyComponentDefinition_SetEndOfFeaturesToTopOrBottom.md) | Sets the End of Part marker to the top or bottom of the browser. |
| [SetOccurrencesProperty](../AssemblyComponentDefinition/AssemblyComponentDefinition_SetOccurrencesProperty.md) | Method that process the property of a collection of occurrences. |
| [SuppressFeatures](../AssemblyComponentDefinition/AssemblyComponentDefinition_SuppressFeatures.md) | Property that returns the SurfaceBodies collection. Surface bodies within the assembly is not currently supported by Inventor. The returned SurfaceBodies collection will be a collection of zero. |
| [TransformOccurrences](../AssemblyComponentDefinition/AssemblyComponentDefinition_TransformOccurrences.md) | Method that transforms a collection of occurrences. |
| [UnsuppressFeatures](../AssemblyComponentDefinition/AssemblyComponentDefinition_UnsuppressFeatures.md) | Method that unsuppresses previously suppressed features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveOccurrence](../AssemblyComponentDefinition/AssemblyComponentDefinition_ActiveOccurrence.md) | Property that returns the that is currently in edit. |
| [AppearanceOverridesObjects](../AssemblyComponentDefinition/AssemblyComponentDefinition_AppearanceOverridesObjects.md) | Property that returns the objects that have appearance overrides in the active design view. The objects returned in the collection can include occurrences. |
| [Application](../AssemblyComponentDefinition/AssemblyComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssemblyEvents](../AssemblyComponentDefinition/AssemblyComponentDefinition_AssemblyEvents.md) | Property returning an AssemblyEvents collection object. |
| [AttributeSets](../AssemblyComponentDefinition/AssemblyComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BIMComponent](../AssemblyComponentDefinition/AssemblyComponentDefinition_BIMComponent.md) | Read-only property that returns the BIMComponent object associated with this component definition. |
| [BOM](../AssemblyComponentDefinition/AssemblyComponentDefinition_BOM.md) | Property that returns the BOM object. |
| [BOMQuantity](../AssemblyComponentDefinition/AssemblyComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../AssemblyComponentDefinition/AssemblyComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../AssemblyComponentDefinition/AssemblyComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [Constraints](../AssemblyComponentDefinition/AssemblyComponentDefinition_Constraints.md) | Property that returns the AssemblyConstraints collection object. |
| [DataIO](../AssemblyComponentDefinition/AssemblyComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [DefaultVirtualComponentMaterial](../AssemblyComponentDefinition/AssemblyComponentDefinition_DefaultVirtualComponentMaterial.md) | Gets and sets the default material associated with the assembly component. This is the material that is used for newly created virtual components. |
| [Document](../AssemblyComponentDefinition/AssemblyComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [FactoryDocument](../AssemblyComponentDefinition/AssemblyComponentDefinition_FactoryDocument.md) | Read-only property that returns the model state factory document when IsModelStateMember returns True. |
| [Features](../AssemblyComponentDefinition/AssemblyComponentDefinition_Features.md) | Gets the Features collection for this assembly (assembly features). |
| [iAssemblyFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_iAssemblyFactory.md) | Property that returns the iAssemblyFactory object. This property will return Nothing in the case where the assembly is not an iAssembly Factory. You can determine this by using the IsiAssemblyFactory property. |
| [iAssemblyMember](../AssemblyComponentDefinition/AssemblyComponentDefinition_iAssemblyMember.md) | Property that returns the iAssemblyMember object. This property will return Nothing in the case where the assembly is not an iAssembly Member. You can determine this by using the IsiAssemblyMember property. |
| [iMateDefinitions](../AssemblyComponentDefinition/AssemblyComponentDefinition_iMateDefinitions.md) | Property that returns the iMateDefinitions collection object associated with this assembly. |
| [iMateResults](../AssemblyComponentDefinition/AssemblyComponentDefinition_iMateResults.md) | Property that returns the iMateResults collection object associated with this assembly. |
| [ImportedComponents](../AssemblyComponentDefinition/AssemblyComponentDefinition_ImportedComponents.md) | Read-only property that returns the ImportedComponents collection object. |
| [IsiAssemblyFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_IsiAssemblyFactory.md) | Property that returns if the assembly is an iAssembly factory or not. It returns True in the case where the assembly is a factory. If True, the factory can be obtained using the iAssemblyFactory property. |
| [IsiAssemblyMember](../AssemblyComponentDefinition/AssemblyComponentDefinition_IsiAssemblyMember.md) | Property that returns if the assembly is an iAssembly Member or not. It returns True in the case where the assembly is a member. If True, the member can be obtained using the iAssemblyMember property. |
| [IsModelStateFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_IsModelStateFactory.md) | Read-only property that returns whether the document is a model state factory document or not. |
| [IsModelStateMember](../AssemblyComponentDefinition/AssemblyComponentDefinition_IsModelStateMember.md) | Read-only property that returns whether the document is a model state member document or not. |
| [Joints](../AssemblyComponentDefinition/AssemblyComponentDefinition_Joints.md) | Read-only property that returns the AssemblyJoints collection object which provides access to the existing joints in the assembly and provides the capability to create new joints. |
| [MassProperties](../AssemblyComponentDefinition/AssemblyComponentDefinition_MassProperties.md) | Property that returns the MassProperties object. This supports performing mass properties calculations for the entire assembly. |
| [ModelAnnotations](../AssemblyComponentDefinition/AssemblyComponentDefinition_ModelAnnotations.md) | Read-only property that returns the ModelAnnotations collection object. |
| [ModelGeometryVersion](../AssemblyComponentDefinition/AssemblyComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [ModelStates](../AssemblyComponentDefinition/AssemblyComponentDefinition_ModelStates.md) | Read-only property that returns the ModelStates object. |
| [OccurrencePatterns](../AssemblyComponentDefinition/AssemblyComponentDefinition_OccurrencePatterns.md) | Method that returns the pattern element this occurrence represents. |
| [Occurrences](../AssemblyComponentDefinition/AssemblyComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../AssemblyComponentDefinition/AssemblyComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [Parameters](../AssemblyComponentDefinition/AssemblyComponentDefinition_Parameters.md) | Property that returns the parameters collection. |
| [Parent](../AssemblyComponentDefinition/AssemblyComponentDefinition_Parent.md) | Property that returns the parent of the object. |
| [PointClouds](../AssemblyComponentDefinition/AssemblyComponentDefinition_PointClouds.md) | Gets the PointClouds collection object that encapsulates all of the point clouds defined in this Component Definition. |
| [PreciseRangeBox](../AssemblyComponentDefinition/AssemblyComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [RangeBox](../AssemblyComponentDefinition/AssemblyComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RepresentationsManager](../AssemblyComponentDefinition/AssemblyComponentDefinition_RepresentationsManager.md) | Property that returns the RepresentationsManager object. |
| [RevitExports](../AssemblyComponentDefinition/AssemblyComponentDefinition_RevitExports.md) | Read-only property that returns the RevitExports collection object. |
| [SimulationManager](../AssemblyComponentDefinition/AssemblyComponentDefinition_SimulationManager.md) | Read-only property that returns the SimulationManager object. This object provides access to the various simulation API’s. |
| [Sketches](../AssemblyComponentDefinition/AssemblyComponentDefinition_Sketches.md) | Gets the Sketches collection for this assembly component. |
| [SurfaceBodies](../AssemblyComponentDefinition/AssemblyComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Type](../AssemblyComponentDefinition/AssemblyComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserCoordinateSystems](../AssemblyComponentDefinition/AssemblyComponentDefinition_UserCoordinateSystems.md) | Property that returns the UserCoordinateSystems collection object. |
| [WorkAxes](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkAxes.md) | Property that returns the WorkAxes collection object that encapsulates all of the work axes defined in this ComponentDefinition. |
| [WorkPlanes](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkPlanes.md) | Property that returns the WorkPlanes collection object that encapsulates all of the work planes defined in this ComponentDefinition. |
| [WorkPoints](../AssemblyComponentDefinition/AssemblyComponentDefinition_WorkPoints.md) | Property that returns the WorkPoints collection object that encapsulates all of the work points defined in this ComponentDefinition. |

## Accessed From

[AngleConstraint.Parent](../AngleConstraint/AngleConstraint_Parent.md), [AngleConstraintProxy.Parent](../AngleConstraintProxy/AngleConstraintProxy_Parent.md), [AssemblyComponentDefinitions.Item](../AssemblyComponentDefinitions/AssemblyComponentDefinitions_Item.md), [AssemblyConstraint.Parent](../AssemblyConstraint/AssemblyConstraint_Parent.md), [AssemblyConstraints.Parent](../AssemblyConstraints/AssemblyConstraints_Parent.md), [AssemblyDocument.ComponentDefinition](../AssemblyDocument/AssemblyDocument_ComponentDefinition.md), [AssemblyJoint.Parent](../AssemblyJoint/AssemblyJoint_Parent.md), [AssemblyJointProxy.Parent](../AssemblyJointProxy/AssemblyJointProxy_Parent.md), [AssemblySymmetryConstraint.Parent](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_Parent.md), [AssemblySymmetryConstraintProxy.Parent](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Parent.md), [CircularOccurrencePattern.Parent](../CircularOccurrencePattern/CircularOccurrencePattern_Parent.md), [CircularOccurrencePatternProxy.Parent](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_Parent.md), [ComponentOccurrence.Parent](../ComponentOccurrence/ComponentOccurrence_Parent.md), [ComponentOccurrenceProxy.Parent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Parent.md), [CustomConstraint.Parent](CustomConstraint_Parent.md), [CustomConstraintProxy.Parent](CustomConstraintProxy_Parent.md), [FeatureBasedOccurrencePattern.Parent](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Parent.md), [FeatureBasedOccurrencePatternProxy.Parent](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_Parent.md), [FlushConstraint.Parent](../FlushConstraint/FlushConstraint_Parent.md), [FlushConstraintProxy.Parent](../FlushConstraintProxy/FlushConstraintProxy_Parent.md), [iAssemblyFactory.Parent](../iAssemblyFactory/iAssemblyFactory_Parent.md), [iAssemblyMember.Parent](../iAssemblyMember/iAssemblyMember_Parent.md), [InsertConstraint.Parent](../InsertConstraint/InsertConstraint_Parent.md), [InsertConstraintProxy.Parent](../InsertConstraintProxy/InsertConstraintProxy_Parent.md), [LayoutConstraint.Parent](../LayoutConstraint/LayoutConstraint_Parent.md), [LayoutConstraintProxy.Parent](../LayoutConstraintProxy/LayoutConstraintProxy_Parent.md), [MateConstraint.Parent](../MateConstraint/MateConstraint_Parent.md), [MateConstraintProxy.Parent](../MateConstraintProxy/MateConstraintProxy_Parent.md), [OccurrencePattern.Parent](../OccurrencePattern/OccurrencePattern_Parent.md), [OccurrencePatterns.Parent](../OccurrencePatterns/OccurrencePatterns_Parent.md), [RectangularOccurrencePattern.Parent](../RectangularOccurrencePattern/RectangularOccurrencePattern_Parent.md), [RectangularOccurrencePatternProxy.Parent](../RectangularOccurrencePatternProxy/RectangularOccurrencePatternProxy_Parent.md), [RevitExport.Parent](../RevitExport/RevitExport_Parent.md), [RigidBodyResults.Parent](RigidBodyResults_Parent.md), [RotateRotateConstraint.Parent](../RotateRotateConstraint/RotateRotateConstraint_Parent.md), [RotateRotateConstraintProxy.Parent](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_Parent.md), [RotateTranslateConstraint.Parent](../RotateTranslateConstraint/RotateTranslateConstraint_Parent.md), [RotateTranslateConstraintProxy.Parent](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_Parent.md), [TangentConstraint.Parent](../TangentConstraint/TangentConstraint_Parent.md), [TangentConstraintProxy.Parent](../TangentConstraintProxy/TangentConstraintProxy_Parent.md), [TransitionalConstraint.Parent](../TransitionalConstraint/TransitionalConstraint_Parent.md), [TransitionalConstraintProxy.Parent](../TransitionalConstraintProxy/TransitionalConstraintProxy_Parent.md), [TranslateTranslateConstraint.Parent](../TranslateTranslateConstraint/TranslateTranslateConstraint_Parent.md), [TranslateTranslateConstraintProxy.Parent](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_Parent.md)

## Derived Classes

[WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |
| [Add assembly mate constraint](../../sample-programs/AssemblyConstraints_AddMateConstraint_Sample.md) | This sample demonstrates the creation of an assembly mate constraint. |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Assembly Ground Occurrences](../../sample-programs/ComponentOccurrence_Grounded_Sample.md) | This sample demonstrates grounding an assembly occurrence. |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |