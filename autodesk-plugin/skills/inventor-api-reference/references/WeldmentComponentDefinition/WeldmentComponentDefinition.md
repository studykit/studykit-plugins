# WeldmentComponentDefinition Object

Derived from: [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md) Object

## Description

The WeldmentComponentDefinition object provides access to all of the assembly and weldment information of a weldment assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AdjustProxyContext](../WeldmentComponentDefinition/WeldmentComponentDefinition_AdjustProxyContext.md) | Returns the specified object proxy scoped into this assembly, trimming any portion of the context from any assembly in which this assembly is a subassembly. In other words, for the given object proxy, this method makes a new object proxy which has this component definition as the context definition. |
| [AnalyzeInterference](../WeldmentComponentDefinition/WeldmentComponentDefinition_AnalyzeInterference.md) | Method that analyzes the interference between two components. The input ObjectCollections contain the component occurrences that are to be checked for interference. If only one set is provided then interference checking is performed between all occurrences provided in the set. If two sets are provided then the overlap between the components of the two collections are calculated. |
| [ClearAppearanceOverrides](../WeldmentComponentDefinition/WeldmentComponentDefinition_ClearAppearanceOverrides.md) | Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences. |
| [CreateFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateFactory.md) | Method that converts an assembly to an iAssemblyFactory. The newly created iAssemblyFactory object will have an empty excel spreadsheet. |
| [CreateGeometryIntent](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateGeometryIntent.md) | Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating assembly joints. They are used to identify geometry and specific locations on that geometry. |
| [CreateVisibleOccurrenceFinder](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateVisibleOccurrenceFinder.md) | Method that creates an occurrence finder object that allows you to find all occurrences that are visible or hidden by a defined amount. By default, visible is defined by a portion of the part being visible from any view of the part. Optionally you can specify a camera to limit the viewing angle and the extents. |
| [ExportObjects](../WeldmentComponentDefinition/WeldmentComponentDefinition_ExportObjects.md) | Method that marks all the input objects as exported. |
| [FindUsingPoint](../WeldmentComponentDefinition/WeldmentComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingRay](../WeldmentComponentDefinition/WeldmentComponentDefinition_FindUsingRay.md) | Method that fires a ray through the part or assembly and returns the entities intersected by the ray. The objects intersected by the ray are returned in the order in which they are intersected, with the first entities returned being those closest to the clipping plane. |
| [FindUsingVector](../WeldmentComponentDefinition/WeldmentComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetEndOfFeaturesPosition](../WeldmentComponentDefinition/WeldmentComponentDefinition_GetEndOfFeaturesPosition.md) | Gets the current end of Features position in the browser in an assembly. |
| [GetUnusedGeometries](../WeldmentComponentDefinition/WeldmentComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [HideAllRelationships](../WeldmentComponentDefinition/WeldmentComponentDefinition_HideAllRelationships.md) | Method that hides all of the assembly constraints, joints and iMate objects in the document. |
| [PurgeUnusedGeometries](../WeldmentComponentDefinition/WeldmentComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../WeldmentComponentDefinition/WeldmentComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |
| [SetEndOfFeaturesToTopOrBottom](../WeldmentComponentDefinition/WeldmentComponentDefinition_SetEndOfFeaturesToTopOrBottom.md) | Sets the End of Part marker to the top or bottom of the browser. |
| [SetOccurrencesProperty](../WeldmentComponentDefinition/WeldmentComponentDefinition_SetOccurrencesProperty.md) | Method that process the property of a collection of occurrences. |
| [SuppressFeatures](../WeldmentComponentDefinition/WeldmentComponentDefinition_SuppressFeatures.md) | Property that returns the SurfaceBodies collection. Surface bodies within the assembly is not currently supported by Inventor. The returned SurfaceBodies collection will be a collection of zero. |
| [TransformOccurrences](../WeldmentComponentDefinition/WeldmentComponentDefinition_TransformOccurrences.md) | Method that transforms a collection of occurrences. |
| [UnsuppressFeatures](../WeldmentComponentDefinition/WeldmentComponentDefinition_UnsuppressFeatures.md) | Method that unsuppresses previously suppressed features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveOccurrence](../WeldmentComponentDefinition/WeldmentComponentDefinition_ActiveOccurrence.md) | Property that returns the that is currently in edit. |
| [AppearanceOverridesObjects](../WeldmentComponentDefinition/WeldmentComponentDefinition_AppearanceOverridesObjects.md) | Property that returns the objects that have appearance overrides in the active design view. The objects returned in the collection can include occurrences. |
| [Application](../WeldmentComponentDefinition/WeldmentComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssemblyEvents](../WeldmentComponentDefinition/WeldmentComponentDefinition_AssemblyEvents.md) | Property returning an AssemblyEvents collection object. |
| [AttributeSets](../WeldmentComponentDefinition/WeldmentComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BIMComponent](../WeldmentComponentDefinition/WeldmentComponentDefinition_BIMComponent.md) | Read-only property that returns the BIMComponent object associated with this component definition. |
| [BOM](../WeldmentComponentDefinition/WeldmentComponentDefinition_BOM.md) | Property that returns the BOM object. |
| [BOMQuantity](../WeldmentComponentDefinition/WeldmentComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../WeldmentComponentDefinition/WeldmentComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../WeldmentComponentDefinition/WeldmentComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [Constraints](../WeldmentComponentDefinition/WeldmentComponentDefinition_Constraints.md) | Property that returns the AssemblyConstraints collection object. |
| [DataIO](../WeldmentComponentDefinition/WeldmentComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [DefaultVirtualComponentMaterial](../WeldmentComponentDefinition/WeldmentComponentDefinition_DefaultVirtualComponentMaterial.md) | Gets and sets the default material associated with the assembly component. This is the material that is used for newly created virtual components. |
| [Document](../WeldmentComponentDefinition/WeldmentComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [FactoryDocument](../WeldmentComponentDefinition/WeldmentComponentDefinition_FactoryDocument.md) | Read-only property that returns the model state factory document when IsModelStateMember returns True. |
| [Features](../WeldmentComponentDefinition/WeldmentComponentDefinition_Features.md) | Gets the Features collection for this assembly (assembly features). |
| [iAssemblyFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_iAssemblyFactory.md) | Property that returns the iAssemblyFactory object. This property will return Nothing in the case where the assembly is not an iAssembly Factory. You can determine this by using the IsiAssemblyFactory property. |
| [iAssemblyMember](../WeldmentComponentDefinition/WeldmentComponentDefinition_iAssemblyMember.md) | Property that returns the iAssemblyMember object. This property will return Nothing in the case where the assembly is not an iAssembly Member. You can determine this by using the IsiAssemblyMember property. |
| [iMateDefinitions](../WeldmentComponentDefinition/WeldmentComponentDefinition_iMateDefinitions.md) | Property that returns the iMateDefinitions collection object associated with this assembly. |
| [iMateResults](../WeldmentComponentDefinition/WeldmentComponentDefinition_iMateResults.md) | Property that returns the iMateResults collection object associated with this assembly. |
| [ImportedComponents](../WeldmentComponentDefinition/WeldmentComponentDefinition_ImportedComponents.md) | Read-only property that returns the ImportedComponents collection object. |
| [IsiAssemblyFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_IsiAssemblyFactory.md) | Property that returns if the assembly is an iAssembly factory or not. It returns True in the case where the assembly is a factory. If True, the factory can be obtained using the iAssemblyFactory property. |
| [IsiAssemblyMember](../WeldmentComponentDefinition/WeldmentComponentDefinition_IsiAssemblyMember.md) | Property that returns if the assembly is an iAssembly Member or not. It returns True in the case where the assembly is a member. If True, the member can be obtained using the iAssemblyMember property. |
| [IsModelStateFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_IsModelStateFactory.md) | Read-only property that returns whether the document is a model state factory document or not. |
| [IsModelStateMember](../WeldmentComponentDefinition/WeldmentComponentDefinition_IsModelStateMember.md) | Read-only property that returns whether the document is a model state member document or not. |
| [Joints](../WeldmentComponentDefinition/WeldmentComponentDefinition_Joints.md) | Read-only property that returns the AssemblyJoints collection object which provides access to the existing joints in the assembly and provides the capability to create new joints. |
| [Machining](../WeldmentComponentDefinition/WeldmentComponentDefinition_Machining.md) | Property that returns the Machining object associated with this Weldment. |
| [MassProperties](../WeldmentComponentDefinition/WeldmentComponentDefinition_MassProperties.md) | Property that returns the MassProperties object. This supports performing mass properties calculations for the entire assembly. |
| [ModelAnnotations](../WeldmentComponentDefinition/WeldmentComponentDefinition_ModelAnnotations.md) | Read-only property that returns the ModelAnnotations collection object. |
| [ModelGeometryVersion](../WeldmentComponentDefinition/WeldmentComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [ModelStates](../WeldmentComponentDefinition/WeldmentComponentDefinition_ModelStates.md) | Read-only property that returns the ModelStates object. |
| [OccurrencePatterns](../WeldmentComponentDefinition/WeldmentComponentDefinition_OccurrencePatterns.md) | Method that returns the pattern element this occurrence represents. |
| [Occurrences](../WeldmentComponentDefinition/WeldmentComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../WeldmentComponentDefinition/WeldmentComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [Parameters](../WeldmentComponentDefinition/WeldmentComponentDefinition_Parameters.md) | Property that returns the parameters collection. |
| [Parent](../WeldmentComponentDefinition/WeldmentComponentDefinition_Parent.md) | Property that returns the parent of the object. |
| [PointClouds](../WeldmentComponentDefinition/WeldmentComponentDefinition_PointClouds.md) | Gets the PointClouds collection object that encapsulates all of the point clouds defined in this Component Definition. |
| [PreciseRangeBox](../WeldmentComponentDefinition/WeldmentComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [Preparations](../WeldmentComponentDefinition/WeldmentComponentDefinition_Preparations.md) | Property that returns the Preparations object associated with this Weldment. |
| [RangeBox](../WeldmentComponentDefinition/WeldmentComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RepresentationsManager](../WeldmentComponentDefinition/WeldmentComponentDefinition_RepresentationsManager.md) | Property that returns the RepresentationsManager object. |
| [RevitExports](../WeldmentComponentDefinition/WeldmentComponentDefinition_RevitExports.md) | Read-only property that returns the RevitExports collection object. |
| [SimulationManager](../WeldmentComponentDefinition/WeldmentComponentDefinition_SimulationManager.md) | Read-only property that returns the SimulationManager object. This object provides access to the various simulation API’s. |
| [Sketches](../WeldmentComponentDefinition/WeldmentComponentDefinition_Sketches.md) | Gets the Sketches collection for this assembly component. |
| [SurfaceBodies](../WeldmentComponentDefinition/WeldmentComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Type](../WeldmentComponentDefinition/WeldmentComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserCoordinateSystems](../WeldmentComponentDefinition/WeldmentComponentDefinition_UserCoordinateSystems.md) | Property that returns the UserCoordinateSystems collection object. |
| [WeldBeadAppearance](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldBeadAppearance.md) | Get and sets current appearance used for the weld beads. Setting to Nothing removes the overrides so that the weld bead uses the appearance associated with the weld material. |
| [WeldBeadAppearanceSourceType](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldBeadAppearanceSourceType.md) | Gets and sets the source of the appearance for the weld bead. Setting to kMaterialAppearance will clear any overrides so that weld bead use the appearance associated with the weld material. |
| [WeldBeadMaterial](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldBeadMaterial.md) | Gets and sets the material of the welds. |
| [WeldEndFillAppearance](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldEndFillAppearance.md) | Gets and sets the currrent appearance used for the end caps of a weld. Setting to Nothing removes the overrides so that the caps use same appearance as the weld beads. |
| [WeldEndFillAppearanceSourceType](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldEndFillAppearanceSourceType.md) | Gets and set the source of the appearance for the end caps of a weld bead. Setting to kWeldsAppearance will clear any overrides so that the caps use same appearance as the weld beads. |
| [Welds](../WeldmentComponentDefinition/WeldmentComponentDefinition_Welds.md) | Property that returns the Welds object. |
| [WeldsComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldsComponentDefinition.md) | Property that returns the associated WeldsComponentDefinition object. |
| [WorkAxes](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkAxes.md) | Property that returns the WorkAxes collection object that encapsulates all of the work axes defined in this ComponentDefinition. |
| [WorkPlanes](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkPlanes.md) | Property that returns the WorkPlanes collection object that encapsulates all of the work planes defined in this ComponentDefinition. |
| [WorkPoints](../WeldmentComponentDefinition/WeldmentComponentDefinition_WorkPoints.md) | Property that returns the WorkPoints collection object that encapsulates all of the work points defined in this ComponentDefinition. |

## Version

Introduced in version 8
