# FlatPatternComponent Object

Derived from: [Component](Component.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

This object represent the root component of a FlatPatternProduct. The flatPattern property will return a FlatPattern object that provides access to the resulting flat pattern geometry.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [allOccurrencesByComponent](FlatPatternComponent_allOccurrencesByComponent.htm) | Returns all occurrences, at any level of the assembly, that reference the specified component. The returned list is read-only. |
| [boundingBox2](FlatPatternComponent_boundingBox2.htm) | Returns the bounding box of the specified entity types within the component. |
| [classType](FlatPatternComponent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createBRepEdgeProfile](FlatPatternComponent_createBRepEdgeProfile.htm) | Creates a profile based on the outside open edges of a BRepFace. |
| [createFlatPattern](FlatPatternComponent_createFlatPattern.htm) | Creates a flat pattern of the sheet metal folded body. The isSheetMetal property of the BRepBody object can be used to determine if a particular body can be flattened. Creating a flat pattern will fail if a flat pattern already exists in the component. You can determine if a flat pattern already exists by checking if the flatPattern property returns a FlatPattern object or null. |
| [createOpenProfile](FlatPatternComponent_createOpenProfile.htm) | Creates an open profile based on the input curve(s). |
| [createThumbnail](FlatPatternComponent_createThumbnail.htm) | Creates a thumbnail for this component. This can be a root component to get a thumbnail that represents the associated file, or it can be any sub component to get a thumbnail of a subset of the complete assembly or individual parts. |
| [findBRepUsingPoint](FlatPatternComponent_findBRepUsingPoint.htm) | Finds all the entities of the specified type at the specified location. |
| [findBRepUsingRay](FlatPatternComponent_findBRepUsingRay.htm) | Finds all the B-Rep entities that are intersected by the specified ray. This can return BRepFace, BrepEdge, and BRepVertex objects. |
| [getPhysicalProperties](FlatPatternComponent_getPhysicalProperties.htm) | Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component. |
| [occurrencesByComponent](FlatPatternComponent_occurrencesByComponent.htm) | Returns all occurrences at the top-level of this component that reference the specified component. The returned list is read-only. |
| [saveCopyAs](FlatPatternComponent_saveCopyAs.htm) | Performs a Save Copy As on this component. This saves the specified component as a new document in the specified location. |
| [transformOccurrences](FlatPatternComponent_transformOccurrences.htm) | Transforms a set of occurrences in one step. This provides better performance than transforming them one at a time. This method is only valid when called on the root component because Fusion flattens the entire assembly structure when manipulating the assembly so all transforms are relative to the root component. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [activeSheetMetalRule](FlatPatternComponent_activeSheetMetalRule.htm) | Gets and sets the active sheet metal rule. This can return null in the case where the component has never contained any sheet metal related data. |
| [allAsBuiltJoints](FlatPatternComponent_allAsBuiltJoints.htm) | Returns all joint origins in this component and any sub components. The joint origins returned are all in the context of this component so any joint origins in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joint origins, when manipulating an assembly. |
| [allAssemblyConstraints](FlatPatternComponent_allAssemblyConstraints.htm) | Returns all assembly constraints in this component and any sub components. The assembly constraints returned are all in the context of this component so any joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joints, when manipulating an assembly. |
| [allJointOrigins](FlatPatternComponent_allJointOrigins.htm) | Returns all as-built joints in this component and any sub components. The as-built joints returned are all in the context of this component so any as-built joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including as-built joints, when manipulating an assembly. |
| [allJoints](FlatPatternComponent_allJoints.htm) | Returns all joints in this component and any sub components. The joints returned are all in the context of this component so any joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joints, when manipulating an assembly. |
| [allOccurrences](FlatPatternComponent_allOccurrences.htm) | Returns all of the occurrences in the assembly regardless of their level within the assembly structure. The returned list is read-only. |
| [allRigidGroups](FlatPatternComponent_allRigidGroups.htm) | Returns all rigid groups in this component and any sub components. The rigid groups returned are all in the context of this component so any rigid groups in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including rigid groups, when manipulating an assembly. |
| [allTangentRelationships](FlatPatternComponent_allTangentRelationships.htm) | Returns all tangent relationships in this component and any sub components. The tangent relationships returned are all in the context of this component so any tangent relationships in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including tangent relationships, when manipulating an assembly. |
| [asBuiltJoints](FlatPatternComponent_asBuiltJoints.htm) | Returns the collection of as-built joints associated with this component. |
| [assemblyConstraints](FlatPatternComponent_assemblyConstraints.htm) | Returns the collection of assembly constraints associated with this component. |
| [attributes](FlatPatternComponent_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](FlatPatternComponent_boundingBox.htm) | Returns the bounding box of this component. This is always in world space of the component. The boundingBox2 method provides greater control over which types of entities you want included in the bounding box calculation. |
| [bRepBodies](FlatPatternComponent_bRepBodies.htm) | Returns the B-Rep bodies collection associated with this component. |
| [canvases](FlatPatternComponent_canvases.htm) | Returns the canvases collection associated with this component. This provides access to the existing canvases and supports the creation of new canvases. |
| [componentColor](FlatPatternComponent_componentColor.htm) | Gets and sets the color associated with a component. This color is only used when the "Display Component Colors" command is enabled. Enabling the display of component colors is done through the command or API using the Application.isComponentColorsDisplayed property. When this is on, all bodies in a component will display using the color assigned to the component. Fusion randomly assigns a color to a component when it is created. This property allows you to get and change the assigned default color. Setting this property to null results in a new color being randomly assigned by Fusion. This is the equivalent of the "Cycle Component Color" command available in the context menu of a component. |
| [constructionAxes](FlatPatternComponent_constructionAxes.htm) | Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes. |
| [constructionPlanes](FlatPatternComponent_constructionPlanes.htm) | Returns the construction planes collection associated with this component. This provides access to the existing construction planes and supports the creation of new construction planes. |
| [constructionPoints](FlatPatternComponent_constructionPoints.htm) | Returns the construction points collection associated with this component. This provides access to the existing construction points and supports the creation of new construction points. |
| [customGraphicsGroups](FlatPatternComponent_customGraphicsGroups.htm) | Returns the customGraphicsGroups object in this component. |
| [dataComponent](FlatPatternComponent_dataComponent.htm) | ![Preview](../images/TestTubeSmall.png)Returns the DataComponent associated with this component. The DataComponent provides ID information that can be used to access this component using the MFG DM API. These ID's don't exist until a component has been saved. The ID's are generated by MFG DM API on the cloud, so there will be a slight delay after saving before the ID's are available. This property returns null in the case the MFG DM API information doesn't exist yet. |
| [decals](FlatPatternComponent_decals.htm) | Returns the decals collection associated with this component. This provides access to the existing decals and supports the creation of new decals. |
| [description](FlatPatternComponent_description.htm) | Gets and sets the description associated with this component. |
| [entityToken](FlatPatternComponent_entityToken.htm) | Returns a token for the Component object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same component.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [features](FlatPatternComponent_features.htm) | Returns the collection that provides access to all of the features associated with this component. |
| [flatPattern](FlatPatternComponent_flatPattern.htm) | Gets the existing flat pattern or returns null in the case where a flat pattern doesn't exist in this component. |
| [id](FlatPatternComponent_id.htm) | Returns the persistent ID of the component. This ID is created with the component and does not change. Because this ID does not change, different revisions of the same design or copies of the design asset/file will retain this ID. If components from different designs have the same ID, it indicates they are either different revisions or a copy of the design was made. Therefore, this ID will always be unique within a single design, but may not be unique in an assembly where externally referenced designs include different revisions or copies of a design.   The ID is also the same ID used by PIM (Product Information Model). |
| [isBodiesFolderLightBulbOn](FlatPatternComponent_isBodiesFolderLightBulbOn.htm) | Gets and sets if the light bulb of the bodies folder as seen in the browser is on or off. This controls the visibility of the solid/surface bodies and the mesh bodies in this component. |
| [isCanvasFolderLightBulbOn](FlatPatternComponent_isCanvasFolderLightBulbOn.htm) | Gets and sets if the light bulb of the canvas folder as seen in the browser is on or off. This controls the visibility of all the canvases in the component. |
| [isConstructionFolderLightBulbOn](FlatPatternComponent_isConstructionFolderLightBulbOn.htm) | Gets and sets if the light bulb of the construction folder as seen in the browser is on or off. This controls the visibility of the (non-origin) construction geometry (i.e. planes, points, axes). |
| [isDecalFolderLightBulbOn](FlatPatternComponent_isDecalFolderLightBulbOn.htm) | Gets and sets whether the light bulb of the decal folder, as seen in the browser, is on or off. This controls the visibility of all the decals in the component. |
| [isJointOriginsFolderLightBulbOn](FlatPatternComponent_isJointOriginsFolderLightBulbOn.htm) | Gets and sets if the light bulb of the joint origins folder as seen in the browser is on or off. This controls the visibility of the joint origins in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component. |
| [isJointsFolderLightBulbOn](FlatPatternComponent_isJointsFolderLightBulbOn.htm) | Gets and sets if the light bulb of the joints folder as seen in the browser is on or off. This controls the visibility of the joints in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component. |
| [isLibraryItem](FlatPatternComponent_isLibraryItem.htm) | Gets whether the component was created from a fasteners library item." |
| [isOriginFolderLightBulbOn](FlatPatternComponent_isOriginFolderLightBulbOn.htm) | Gets and sets if the light bulb of the origin folder as seen in the browser is on or off. This controls the visibility of the origin construction geometry. |
| [isSketchFolderLightBulbOn](FlatPatternComponent_isSketchFolderLightBulbOn.htm) | Gets and sets if the light bulb of the sketch folder as seen in the browser is on or off. This controls the visibility of the sketches in this component. |
| [isValid](FlatPatternComponent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [jointOrigins](FlatPatternComponent_jointOrigins.htm) | Returns the collection of joint origins associated with this component. |
| [joints](FlatPatternComponent_joints.htm) | Returns the collection of joints associated with this component. |
| [material](FlatPatternComponent_material.htm) | Gets and sets the physical material assigned to this component. |
| [meshBodies](FlatPatternComponent_meshBodies.htm) | Returns the mesh bodies collection associated with this component. |
| [mfgdmModelId](FlatPatternComponent_mfgdmModelId.htm) | ![Preview](../images/TestTubeSmall.png)Returns the MFGDM model ID for this component. |
| [modelParameters](FlatPatternComponent_modelParameters.htm) | Returns the collection of model parameters in the Component. |
| [name](FlatPatternComponent_name.htm) | Property that gets and sets the name of this component. This is the name shown in the browser for each occurrence referencing this component. |
| [objectType](FlatPatternComponent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [occurrences](FlatPatternComponent_occurrences.htm) | Property that returns the Occurrences collection associated with this component. This provides access to the occurrences at the top-level of this component and provides the functionality to add new occurrences. |
| [opacity](FlatPatternComponent_opacity.htm) | Gets and sets the opacity override assigned to this component. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.   This is only applicable for a non-root local component.   This value is not necessarily related to what the user sees because the opacity is inherited. For example, if you have TopComponent and it has a component in it called SubComponent and you set the opacity of TopComponent to be 0.5, SubComponent will also be shown as slightly transparent even though the opacity property for it will return 1.0. Because a component can be referenced as an occurrence in other components and they can have different opacity settings, it's possible that different instances of the same component can display using different opacity levels. To get the opacity that it is being displayed with use the Occurrence.visibleOpacity property. |
| [orientedMinimumBoundingBox](FlatPatternComponent_orientedMinimumBoundingBox.htm) | Returns an oriented bounding box that is best oriented to tightly fit all B-Rep bodies in the component. All other geometry types are ignored. |
| [originConstructionPoint](FlatPatternComponent_originConstructionPoint.htm) | Returns the origin construction point. |
| [parentDesign](FlatPatternComponent_parentDesign.htm) | Returns the parent product this component is owned by. |
| [partNumber](FlatPatternComponent_partNumber.htm) | Gets and sets the part number associated with this component. Setting this to an empty string will reset it to be the same as the component name. |
| [physicalProperties](FlatPatternComponent_physicalProperties.htm) | Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component. Property values will be calculated using the 'LowCalculationAccuracy' setting when using this property to get the PhysicalProperties object. To specify a higher calculation tolerance, use the getPhysicalProperties method instead. |
| [preciseBoundingBox](FlatPatternComponent_preciseBoundingBox.htm) | Returns a bounding box that tightly fits around all B-Rep bodies in the component. All other geometry types are ignored. |
| [propertyGroups](FlatPatternComponent_propertyGroups.htm) | Returns the PropertyGroups object associated with this component. |
| [revisionId](FlatPatternComponent_revisionId.htm) | Returns the current revision ID of the component. This ID changes any time the component is modified in any way. By getting and saving the ID when you create any data that is dependent on the component, you can then compare the saved ID with the current ID to determine if the component has changed to know if you should update your data. |
| [rigidGroups](FlatPatternComponent_rigidGroups.htm) | Returns the collection of rigid groups associated with this component. |
| [sketches](FlatPatternComponent_sketches.htm) | Returns the sketches collection associated with this component. This provides access to the existing sketches and supports the creation of new sketches. |
| [tangentRelationships](FlatPatternComponent_tangentRelationships.htm) | Returns the collection of tangent relationships associated with this component. |
| [xConstructionAxis](FlatPatternComponent_xConstructionAxis.htm) | Returns the X origin construction axis. |
| [xYConstructionPlane](FlatPatternComponent_xYConstructionPlane.htm) | Returns the XY origin construction plane. |
| [xZConstructionPlane](FlatPatternComponent_xZConstructionPlane.htm) | Returns the XZ origin construction plane. |
| [yConstructionAxis](FlatPatternComponent_yConstructionAxis.htm) | Returns the Y origin construction axis. |
| [yZConstructionPlane](FlatPatternComponent_yZConstructionPlane.htm) | Returns the YZ origin construction plane. |
| [zConstructionAxis](FlatPatternComponent_zConstructionAxis.htm) | Returns the Z origin construction axis. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |