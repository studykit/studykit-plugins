# Design Object

Derived from: [Product](Product.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Object that represents an open Fusion design. This derives from the Product base class and adds the Fusion functionality specific to a Design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activateRootComponent](Design_activateRootComponent.htm) | Makes the root component the active component in the user interface. This is the same as enabling the radio button next to the root component in the browser. |
| [analyzeInterference](Design_analyzeInterference.htm) | Calculates the interference between the input bodies and/or occurrences. |
| [areaProperties](Design_areaProperties.htm) | Returns the AreaProperties object that has properties for getting the area, perimeter, centroid, etc for a collection of 2D sketch profiles and/or planar surfaces that all lie on the same plane. |
| [classType](Design_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [computeAll](Design_computeAll.htm) | Forces a recompute of the entire design. This is the equivalent of the "Compute All" command. |
| [createConfiguredDesign](Design_createConfiguredDesign.htm) | Converts this design into a configured design. The returned ConfigurationTable has a single row and no columns. You can use it to add columns and rows to define the configuration. |
| [createInterferenceInput](Design_createInterferenceInput.htm) | Creates an InterferenceInput object. This object collects the entities and options that are used when calculating interference. To analyze interference you first create an InterferenceInput supplying the entities and set any other settings and then provide this object as input to the analyzeInterference method. |
| [deleteEntities](Design_deleteEntities.htm) | Deletes the specified set of entities that are associated with this product. |
| [findAttributes](Design_findAttributes.htm) | Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product. |
| [findEntityByToken](Design_findEntityByToken.htm) | Returns the entities associated with the provided token. The return is an array of entities. In most cases an array containing a single entity will be returned but there are cases where more than one entity can be returned. An example of this is where a token is obtained from a face and subsequent modeling operations cause the face to be split into two or more pieces. All of the faces that represent the original face will be returned with the first face being the most logical match to the original face. |
| [modifyParameters](Design_modifyParameters.htm) | Modifies the values of many parameters all at once. Changing them all at once is more efficient than modifying them one at a time. |
| [physicalProperties](Design_physicalProperties.htm) | Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc for a collection of 3D solid objects. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [activeComponent](Design_activeComponent.htm) | Returns the component that is current being edited. This can return the root component or another component within the design. |
| [activeEditObject](Design_activeEditObject.htm) | Returns the current edit target as seen in the user interface. This edit target is defined as the container object that will be added to if something is created. For example, a component can be an edit target so that when new bodies are created they are added to that component. A sketch can also be an edit target. |
| [activeOccurrence](Design_activeOccurrence.htm) | Returns the occurrence that is currently activated, if any. This can return null in the case where no occurrence is activated and the root component is active. |
| [allComponents](Design_allComponents.htm) | Returns the Components collection that provides access to existing components in a design. |
| [allParameters](Design_allParameters.htm) | Returns a read only list of all parameters in the design. This includes the user parameters and model parameters from all components in this design. The parameters from Externally Referenced components are NOT included because they are in actuality, separate designs. |
| [analyses](Design_analyses.htm) | Gets the collection of design analyses associated with this design. |
| [appearances](Design_appearances.htm) | Returns the appearances contained in this document. |
| [attributes](Design_attributes.htm) | Returns the collection of attributes associated with this product. |
| [configurationRowId](Design_configurationRowId.htm) | Returns the ID of the row that defines this configuration. Use the isCongiguration property to determine if this Design is a configuration or not. If this is not a configuration, this property returns an empty string. |
| [configurationTopTable](Design_configurationTopTable.htm) | If this design is a configured design or a configuration, this property returns the associated ConfigurationTopTable object. If this is not a configured design or configuration, this property returns null. |
| [contactSets](Design_contactSets.htm) | Returns the contact sets associated with this design. |
| [designPlasticRules](Design_designPlasticRules.htm) | Gets the collection of plastic rules in the design. |
| [designSheetMetalRules](Design_designSheetMetalRules.htm) | Gets the collection of sheet metal rules in the design. |
| [designType](Design_designType.htm) | Gets and sets the current design type (DirectDesignType or ParametricDesignType) Changing an existing design from ParametricDesignType to DirectDesignType will result in the timeline and all design history being removed and further operations will not be captured in the timeline. |
| [exportManager](Design_exportManager.htm) | Returns the ExportManager for this design. You use the ExportManager to export the current design in various formats. |
| [fusionUnitsManager](Design_fusionUnitsManager.htm) | Returns a specialized UnitsManager that can set the default length units and work with parameters. |
| [isConfiguration](Design_isConfiguration.htm) | Gets if this design is a configuration. If this returns true, the configurationRowId can be used to get the row used to define this configuration. Also, when this is true, the design is essentially read-only and edits are either blocked from taking place or cannot be saved. |
| [isConfiguredDesign](Design_isConfiguredDesign.htm) | Gets if this design is a configured design. A configured design contains a configuration table. Use the configurationTable property to get the associated table. |
| [isContactAnalysisEnabled](Design_isContactAnalysisEnabled.htm) | Gets and sets whether contact analysis is enabled for all components. This is the equivalent of the "Disable Contact / Enable Contact" command. If this if True then any contact analysis defined (either all or contact sets) is enabled. if False, then no contact analysis is performed. |
| [isContactSetAnalysis](Design_isContactSetAnalysis.htm) | Gets and sets whether contact analysis is done using contact sets or between all bodies, independent of any contact sets. If True and the isContactAnalysisEnabled property is True then contact analysis is performed using contact sets. If False and isContactAnalysisEnabled is True, then contact analysis is performed between all bodies. If isContactAnalysisEnabled is False then no contact analysis is performed. |
| [isRootComponentActive](Design_isRootComponentActive.htm) | Gets whether the root component is the active edit target in the user interface. This is the same as checking the state of the radio button next to the root component in the browser. To activate the root component use the ActivateRootComponent method. |
| [isValid](Design_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [libraryPlasticRules](Design_libraryPlasticRules.htm) | Gets the collection of plastic rules in the plastic rule library. |
| [librarySheetMetalRules](Design_librarySheetMetalRules.htm) | Gets the collection of sheet metal rules in the sheet metal rule library. |
| [materials](Design_materials.htm) | Returns the materials contained in this document. |
| [namedViews](Design_namedViews.htm) | Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views. |
| [objectType](Design_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentDocument](Design_parentDocument.htm) | Returns the parent Document object. |
| [productType](Design_productType.htm) | Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property. |
| [renderManager](Design_renderManager.htm) | Returns the RenderManager object associated with this design. Using the RenderManager you can access the same functionality that is available in the Render workspace. |
| [rootComponent](Design_rootComponent.htm) | Returns the root Component. |
| [rootDataComponent](Design_rootDataComponent.htm) | ![Preview](../images/TestTubeSmall.png)Get the root DataComponent in this design. This is only available for top level designs. |
| [selectionSets](Design_selectionSets.htm) | Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets. |
| [snapshots](Design_snapshots.htm) | Returns the Snapshots object associated with this design which provides access to the existing snapshots and the creation of new snapshots. |
| [timeline](Design_timeline.htm) | Returns the timeline associated with this design. |
| [unitsManager](Design_unitsManager.htm) | Returns the UnitsManager object associated with this product. |
| [userParameters](Design_userParameters.htm) | Returns the collection of User Parameters in a design |
| [workspaces](Design_workspaces.htm) | Returns the workspaces associated with this product. |

## Accessed From

[BaseComponent.parentDesign](BaseComponent_parentDesign.htm), [Component.parentDesign](Component_parentDesign.htm), [FlatPatternComponent.parentDesign](FlatPatternComponent_parentDesign.htm), [FusionDocument.design](FusionDocument_design.htm), [FusionUnitsManager.design](FusionUnitsManager_design.htm), [PlasticRule.parentDesign](PlasticRule_parentDesign.htm), [SheetMetalRule.parentDesign](SheetMetalRule_parentDesign.htm), [UserParameter.design](UserParameter_design.htm), [UserParameters.design](UserParameters_design.htm)

## Derived Classes

[FlatPatternProduct](FlatPatternProduct.htm), [WorkingModel](WorkingModel.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Analyze Interference API Sample](AnalyzeInterferenceSample_Sample.htm) | Demonstrates analyzing the interference between components. This uses a direct modeling design because the ability to create bodies that represent the interference volume is only supported in a direct modeling design. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |