# What's New For the September 2025 Release

### Enhancements

1. **Breaking Changes Coming to the New Assembly Constraint Functionality**
   The last release introduced the API for the new assembly constraint functionality. It was a preview feature. In this release, the feature remains a preview, and no changes have been made to the API. However, in the next release, the API for assembly constraints will undergo a complete change. This is why new functionality is released as a preview feature, allowing us to gather feedback about the API or feature while still maintaining the flexibility to make changes. If you've written any code using the existing assembly constraints, be prepared to make adjustments in the next release. The interface is undergoing slight changes, and additional functionality will be added. The names of some of the associated objects will also be changing.
2. **Assembly User Interface Changes**
   In the last release, there was a change to how the assembly functionality is provided in the user interface. It was a preview feature that limited those who could enable it. That option has been removed, and the UI behaves as before. However, a new preview, called "Part and Assembly Design Workflow," has an even greater impact. It's a private preview feature, and for those who have access, it is turned on by default in this release. When this feature is enabled, the UI layout changes, and not all elements are accessible through the API. As a result, some custom commands created by add-ins may not be available. If you are a Fusion Insider, you have access to this new preview and are encouraged to test your commands. If they're not available when the preview is enabled, there's currently no alternative except to disable the preview and revert to the previous UI layout. API access to this new UI layout will be available in the future.
3. **Support for Text Parameters**
   There's new functionality in Fusion that will make many people happy, and there is API support for some of it. The first part of this is the ability to create parameters with text values. The API fully supports creating, querying, and editing these new types of parameters. To support this, when adding a parameter, you can specify the unit type as "Text". Also, the Parameter object now supports the [valueType](Parameter_valueType.htm) and [textValue](Parameter_textValue.htm) properties, so you can determine if a parameter is this new type and get and set the value of the parameter.

   The related piece is the ability to create parametric sketch text that uses parameters. The API doesn't yet support this. Watch for it in an upcoming release.
4. **Full API Support for the Emboss Feature**
   The Emboss feature has been available in Fusion for a long time, but it has had minimal API support. Now, the API provides full support for the [Emboss](EmbossFeatures.htm) feature. You can perform all actions in the API that are available through the user interface. It is a preview feature in this release to allow us to make any needed changes based on feedback, but we don't expect the preview to last long.
5. **Full API Support for Tapped and Clearance Holes**
   This is another case where the functionality has been available in Fusion for quite some time, and the API is now catching up. The API now has full support for tapped and clearance holes. Many new properties have been added to the HoleFeatureInput and HoleInput objects. The full list is shown below.
6. **Thicken Feature Enhancement**
   In this release, Fusion has enhanced the thicken feature to support a rounded thicken, where only sharp thickens were previously supported. A thickenType property is now supported on the [ThickenFeatureInput](ThickenFeatureInput_thickenType.htm) and [ThickenFeature](ThickenFeature_thickenType.htm) objects.
7. **Full Round Fillet Support**
   Here's another one where the API is catching up with the product. The API now has full support for the full round option when creating a fillet feature. Previously, a FullRoundFilletFeature object existed, but it only supported basic feature functionality and lacked support for creating or querying full round fillet features. The FullRoundFilletFeature object has been retired since the full round functionality is now part of the FilletFeature object.
8. **Full API Support for the New Hem Feature**
   There is a new sheet metal feature that most of you may not be aware of yet, as it is a preview feature and is currently only available to a select few. However, the API was implemented concurrently with the feature and is exposed in the API as the [Hem](HemFeatures.htm) feature. Just like the feature, this API is also a preview and could still change before it is released.
9. **Support for Replacing Standard Components in Configurations**
   A new capability supported by configurations is the ability to replace a standard component in an assembly. API supported has also been added through the new [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm), [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm), [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm), and [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm) objects.
10. **Arrange Feature**
    The API for the Arrange feature has graduated from preview to full support.
11. **Part Number and Description Changes**
    This was also in the last "What's New", but because the migration of hubs to support the new collaborative editing is an ongoing process and many of you haven't seen the effects yet, it's being included here again.

    As part of new functionality coming to support [collaborative editing](https://help.autodesk.com/view/fusion360/ENU/?guid=TC-COLLAB-EDIT), some changes have been made to Fusion and the API. The biggest change is that the part number and description properties of the Component object now store and retrieve data from the cloud, rather than the design. This change only applies to files that exist within a hub where concurrent editing has been enabled, so the impact is limited. You can check for this by using the new [DataHub.isCollaborativeEditingEnabled](DataHub_isCollaborativeEditingEnabled.htm) property.

    When this is enabled, there are two things you'll likely notice. The first difference is in performance when using the partNumber and description properties of the Component object. This is because getting and setting these values is no longer a local operation, but rather uses the cloud to perform these tasks.

    Another change is that the cloud data associated with a component, where this data is saved, doesn't exist until the document that contains the component has been saved. The bigger change is that the part number and description can no longer be set until the document containing the component has been saved. These properties can't be set until the document is saved because the component and its properties aren't available on the cloud until the document is saved. You can read more about this in the new [MFGDM API user manual topic](MFGDMAPI_UM.htm).
12. **Additional Mesh Feature Support**
    A significant portion of the Mesh functionality was released as preview functionality in the last release. There was an oversight that the properties to access three of the features were missing on the Features collection object. This has been corrected with the addition of the [Features.meshConvertFeatures](Features_meshConvertFeatures.htm), [Features.meshSeparateFeatures](Features_meshSeparateFeatures.htm), and [Features.meshReverseNormalFeatures](Features_meshReverseNormalFeatures.htm) properties.
13. **Control the Visibility of JointOrigins**
    The [isJointOriginsFolderLightBulbOn](Component_isJointOriginsFolderLightBulbOn.htm) has been added to the Component object so you can turn on/off the display of all joint origins in a component.
14. **User Manual Update for Icons**
    The [Command Icons](UserInterface_UM.htm#IconsForCommands) section of the User Interface topic in the API User Manual has been updated with the latest information regarding SVG file support and icons for the various user interface themes.

### CAM API Changes

1. The CAMParameter object has been enhanced with several new properties: [fullTitle](CAMParameter_fullTitle.htm), [isVisible](CAMParameter_isVisible.htm), [userDefaultExpression](CAMParameter_userDefaultExpression.htm), [systemDefaultExpression](CAMParameter_systemDefaultExpression.htm), and [saveExpressionAsUserDefault](CAMParameter_saveExpressionAsUserDefault.htm). Also, the method [CAMParameters.resetToSystemDefaults](CAMParameters_resetToSystemDefaults.htm) was added to reset all parameters to their default values.
2. The CAMLibrary object now supports the [doesPathExist](CAMLibrary_doesPathExist.htm) method to make it easy to check if a path exists.
3. A lot of new functionality was added to support defining machines using the API. You can see a long list below.

### Fixes

1. When using the Documents.open method, there is an argument to specify whether the document should be opened visibly. This worked quite a while ago, but has been broken. It now functions as expected and will open a document invisibly.
2. design\_oneBETU4 reported a problem on the [forum](https://forums.autodesk.com/t5/fusion-api-and-scripts-forum/can-t-get-sketchtext-eplode-method-to-return-curves-in-python/td-p/13671798) about getting back results when exploding text in a sketch. This has been fixed.
3. alasdair\_scott2DJBH reported a problem on the [forum](https://forums.autodesk.com/t5/fusion-api-and-scripts-forum/api-bug-occurrence-islightbulbon-did-not-work-properly/td-p/9531468) about isLightBulbOn property of the Occurrence object not behaving correctly. It works now.

### Custom Features

Custom Features is a new functionality that is currently in preview. This release has nothing new for custom features, but we still encourage you to try it and let us know your thoughts. You can learn more about it in the [Custom Feature](CustomFeatures_UM.htm) topic in the API User Manual. There are also two add-in samples referenced in that document that you can use to see the functionality.

This functionality is provided as a preview of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the [Fusion API and Scripts Forum](https://forums.autodesk.com/t5/fusion-api-and-scripts-forum/bd-p/fusion-api-scripts-forum-en). However, because this previews future functionality, it may change, breaking any existing programs that use it. Therefore, you should never deliver programs that utilize any preview capabilities.

## New Objects

|  |  |
| --- | --- |
| Name | Description |
| [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) | This object provides methods to query the clearance hole to find valid definitions for creating a clearance hole. |
| [ClearanceHoleInfo](ClearanceHoleInfo.htm) | This object defines the methods and properties that define the size of a clearance hole. This object is used to create new hole features whose size is defined as a clearance hole for a specific size fastener. A new ClearanceHoleInfo object is created by using the ClearanceHoleInfo.create method. To determine valid values when creating a ClearanceHoleInfo object, you can use the ClearanceHoleDataQuery object, which is statically created using the ClearanceHoleDataQuery.create method. |
| [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm) | Represents a single cell within a top or custom theme configuration table that controls which design is used for an inserted standard design. Use the parent column to get the occurrence being modified. |
| [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm) | This object represents a column in the table that controls which design should be referenced by an occurrence. The column contains a list of designs that have been specified for that column. One of the designs is specified for each cell in the column. That design will be referenced by the occurrence when the row that cell is in is active. |
| [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm) | This object represents an individual ConfigurationReplaceDesign object that has been defined for a ConfigurationReplaceDesignColumn. Multiple ConfigurationReplaceDesign objects can be defined for a column and then one of those ConfigurationReplaceDesign objects is specified in each cell of the column. |
| [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) | Collection object that provides access to all the ConfigurationReplaceDesign objects that have been defined for a ConfigurationReplaceDesignColumn. You can also use this collection to define new replace designs that will then be available when specifying which design to use in a cell. |
| [DoubleHemFeatureDefinition](DoubleHemFeatureDefinition.htm) | The definition for a double hem. |
| [EmbossFeature](EmbossFeature.htm) | Object that represents an existing emboss feature in a design. |
| [EmbossFeatureInput](EmbossFeatureInput.htm) | This class defines the methods and properties that pertain to the definition of an emboss feature. |
| [EmbossFeatures](EmbossFeatures.htm) | Collection that provides access to all of the existing emboss features in a component and supports the ability to create new emboss features. |
| [FlatHemFeatureDefinition](FlatHemFeatureDefinition.htm) | The definition for a flat hem. |
| [FullRoundFilletFaceSet](FullRoundFilletFaceSet.htm) | The class for the full round fillet face set. |
| [FullRoundFilletFaceSets](FullRoundFilletFaceSets.htm) | Collection that provides access to all existing full round fillet face sets associated with a full round fillet feature or a FullRoundFilletFeatureInput object, and allows adding new full round fillet face sets. |
| [FullRoundFilletFeatureInput](FullRoundFilletFeatureInput.htm) | This class defines the methods and properties that pertain to the definition of a full round fillet feature. |
| [HemFeature](HemFeature.htm) | Defines a hem feature, providing methods to redefine the type of hem. |
| [HemFeatureDefinition](HemFeatureDefinition.htm) | A Base class to return the information used to define the HemFeature. |
| [HemFeatureInput](HemFeatureInput.htm) | This class defines the methods and properties that pertain to the definition of a hem feature. |
| [HemFeatures](HemFeatures.htm) | Collection that provides access to all of the existing hem features in a design and supports the ability to create new hem features. |
| [InteractionsMachineElement](InteractionsMachineElement.htm) | Machine element representing the machine's interactions. This controls how MachineItems interact with each other. |
| [MachineElementInput](MachineElementInput.htm) | Base class for machine element inputs. |
| [MachineInteractionPair](MachineInteractionPair.htm) | MachineInteractionPair objects control how a pair of MachineItems interact with each other. |
| [MachineItem](MachineItem.htm) | An item on a machine that can collide. That is, a MachinePart, or something attached to a MachinePart. Create them via InteractionsMachineElement::createMachineItem |
| [MultiAxisCombinationDPMFeedrateSettings](MultiAxisCombinationDPMFeedrateSettings.htm) | Specialization of MultiAxisDPMFeedrateSettings for degrees per minute feedrates that require a combination of linear and rotary movements. |
| [MultiAxisDPMFeedrateSettings](MultiAxisDPMFeedrateSettings.htm) | Specialization of MultiAxisFeedrateSettings for standard degrees per minute feedrates. |
| [MultiAxisFeedrateSettings](MultiAxisFeedrateSettings.htm) | Base class for the multi-axis feedrate settings |
| [MultiAxisFeedrateSettingsInput](MultiAxisFeedrateSettingsInput.htm) | Input class for creating MultiAxisFeedrateSettings objects. |
| [MultiAxisInverseTimeFeedrateSettings](MultiAxisInverseTimeFeedrateSettings.htm) | Specialization of MultiAxisFeedrateSettings for inverse time feedrates. |
| [MultiAxisMachineElement](MultiAxisMachineElement.htm) | Machine element representing multi-axis machine settings. |
| [MultiAxisMachineElementInput](MultiAxisMachineElementInput.htm) | Specialization of MachineElementInput for creating a multi-axis machine element. |
| [MultiAxisProgrammedFeedrateSettings](MultiAxisProgrammedFeedrateSettings.htm) | Specialization of MultiAxisFeedrateSettings for programmed feedrates. |
| [MultiAxisRetractAndReconfigureSettings](MultiAxisRetractAndReconfigureSettings.htm) | Settings for multi-axis retract and reconfigure. |
| [MultiAxisSingularityLinearizationSettings](MultiAxisSingularityLinearizationSettings.htm) | The class for the multi-axis singularity linearization settings. |
| [MultiAxisSingularitySettings](MultiAxisSingularitySettings.htm) | Base class for multi-axis singularity settings. |
| [OpenHemFeatureDefinition](OpenHemFeatureDefinition.htm) | The definition for an open hem. |
| [RolledHemFeatureDefinition](RolledHemFeatureDefinition.htm) | The definition for a rolled hem. |
| [RopeHemFeatureDefinition](RopeHemFeatureDefinition.htm) | The definition for a rope hem. |
| [TeardropHemFeatureDefinition](TeardropHemFeatureDefinition.htm) | The definition for a teardrop hem. |
| [ToolingCapabilitiesMachineElement](ToolingCapabilitiesMachineElement.htm) | Machine element representing the tooling capabilities of a machine. |
| [ToolingCapabilitiesMachineElementInput](ToolingCapabilitiesMachineElementInput.htm) | Input class for creating ToolingCapabilitiesMachineElement objects. |

## New Methods, Properties and Events

|  |  |
| --- | --- |
| Name | Description |
| [AdditivePlatformMachineElement.cornerRadius](AdditivePlatformMachineElement_cornerRadius.htm) | Radius used to round the corners of the build platform. Units are cm. |
| [CAMLibrary.doesPathExist](CAMLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [CAMParameter.fullTitle](CAMParameter_fullTitle.htm) | Returns the full title of this parameter as seen in the user interface. This can potentially be more descriptive than the basic title. This title is localized and can change based on the current language. |
| [CAMParameter.isVisible](CAMParameter_isVisible.htm) | Gets if this parameter is visible in the user interface. |
| [CAMParameter.saveExpressionAsUserDefault](CAMParameter_saveExpressionAsUserDefault.htm) | Saves the current expression as user default value. Throws an exception if the parent is not an operation or does not support user default expressions. |
| [CAMParameter.systemDefaultExpression](CAMParameter_systemDefaultExpression.htm) | Returns the systemDefaultExpression of this parameter. |
| [CAMParameter.userDefaultExpression](CAMParameter_userDefaultExpression.htm) | Gets and sets the userDefaultExpression of this parameter. If no userDefaultExpression is set, the systemDefaultExpression is returned. Throws an exception if the parent is not an operation or does not support user default expressions. |
| [CAMParameters.resetToSystemDefaults](CAMParameters_resetToSystemDefaults.htm) | Resets each parameter to its system default. |
| [CAMTemplateLibrary.doesPathExist](CAMTemplateLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [Component.isJointOriginsFolderLightBulbOn](Component_isJointOriginsFolderLightBulbOn.htm) | Gets and sets if the light bulb of the joint origins folder as seen in the browser is on or off. This controls the visibility of the joint origins in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component. |
| [ConfigurationColumns.addInsertStandardDesignColumn](ConfigurationColumns_addInsertStandardDesignColumn.htm) | Add a new column to control which standard design is used for an inserted design. If an inserted column already exists for the occurrence, the existing column is returned. |
| [ControllerConfigurationMachineElement.nonTcpRapidInterpolationMode](ControllerConfigurationMachineElement_nonTcpRapidInterpolationMode.htm) | Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is inactive, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. |
| [ControllerConfigurationMachineElement.tcpRapidInterpolationMode](ControllerConfigurationMachineElement_tcpRapidInterpolationMode.htm) | Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is active, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. Tool Tip adjusts the linear axes to keep the tool's tip positioned along the direct line between the start and finish points. |
| [CustomFeatureParameter.textValue](CustomFeatureParameter_textValue.htm) | Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [CustomFeatureParameter.valueType](CustomFeatureParameter_valueType.htm) | Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |
| [Features.embossFeatures](Features_embossFeatures.htm) | Returns the collection that provides access to the emboss features within the component and supports the creation of new emboss features. |
| [Features.hemFeatures](Features_hemFeatures.htm) | Returns the collection that provides access to the existing Hem features. |
| [Features.meshConvertFeatures](Features_meshConvertFeatures.htm) | Returns the collection that provides access to the mesh convert features within the component and supports the creation of new mesh convert features. |
| [Features.meshReverseNormalFeatures](Features_meshReverseNormalFeatures.htm) | Returns the collection that provides access to the mesh reverse normal features within the component and supports the creation of new mesh reverse normal features. |
| [Features.meshSeparateFeatures](Features_meshSeparateFeatures.htm) | Returns the collection that provides access to the mesh separate features within the component and supports the creation of new mesh separate features. |
| [FilletFeature.convert](FilletFeature_convert.htm) | Method that converts this feature to another fillet feature type. |
| [FilletFeature.filletFeatureType](FilletFeature_filletFeatureType.htm) | Returns the FilletFeatureTypes indicating this fillet feature type. |
| [FilletFeature.fullRoundFilletFaceSets](FilletFeature_fullRoundFilletFaceSets.htm) | Returns the full round fillet face sets collection associated with this fillet feature. This collection is only valid when the filletFeatureType is FullRoundFilletFeatureType and it returns null if the filletFeatureType is not FullRoundFilletFeatureType. |
| [FilletFeatures.addFullRoundFillet](FilletFeatures_addFullRoundFillet.htm) | Creates a new full round fillet feature. |
| [FilletFeatures.createFullRoundFilletInput](FilletFeatures_createFullRoundFilletInput.htm) | Creates a FullRoundFilletFeatureInput object. Use properties and methods on this object to define the fillet you want to create and then use the addFullRoundFillet method, passing in the FullRoundFilletFeatureInput object. |
| [FlatPatternComponent.isJointOriginsFolderLightBulbOn](FlatPatternComponent_isJointOriginsFolderLightBulbOn.htm) | Gets and sets if the light bulb of the joint origins folder as seen in the browser is on or off. This controls the visibility of the joint origins in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component. |
| [FusionProductPreferences.isAutoLookAtSketch2](FusionProductPreferences_isAutoLookAtSketch2.htm) | Gets and sets if the view is re-oriented to view the newly created sketch, and if it is re-oriented, if the camera uses the current camera settings or is orthographic. |
| [HoleFeature.clearanceHoleInfo](HoleFeature_clearanceHoleInfo.htm) | Returns the information used to define a clearance hole. This returns a ClearanceHoleInfo object when the holeTapType returns ClearanceHoleTapType. Otherwise this property returns null. |
| [HoleFeature.holeTapType](HoleFeature_holeTapType.htm) | This property returns the current type of tap associated with this hole. You can set the tap type by using one of the following methods: setToSimpleHole, setToClearanceHole, or setToTappedHole. |
| [HoleFeature.setToClearanceHole](HoleFeature_setToClearanceHole.htm) | Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object. |
| [HoleFeature.setToSimpleHole](HoleFeature_setToSimpleHole.htm) | This method sets the hole's tap to be "simple," which means that the hole will not have any tap and will be a simple hole. |
| [HoleFeature.setToTappedHole](HoleFeature_setToTappedHole.htm) | Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object. |
| [HoleFeature.tappedHoleInfo](HoleFeature_tappedHoleInfo.htm) | This property returns the information used to define a tapped hole. Otherwise, this property returns null. |
| [HoleFeature.thread](HoleFeature_thread.htm) | When a tapped hole is created, a thread feature is also automatically created and controls the tapped threads. The thread feature is tied to the hole and is not displayed in the timeline and is suppressed if the hole is suppressed and deleted if the hole is deleted. This property returns the thread feature associated with this hole if it is a tapped hole. It returns null for all other hole types. |
| [HoleFeatureInput.holeTapType](HoleFeatureInput_holeTapType.htm) | Returns the current type of tap associated with this hole. When a new HoleFeatureInput is created, this will default to SimpleHoleTapType, which means the hole will not have any tap and will be a simple hole. You can set the tap type by using one of the methods to define the specific tap desired. |
| [HoleFeatureInput.isFullLength](HoleFeatureInput_isFullLength.htm) | Gets and sets if this thread is the full length of the hole. It defaults to true. |
| [HoleFeatureInput.isModeled](HoleFeatureInput_isModeled.htm) | Gets and sets if the thread is physical or cosmetic thread. A value of true indicates a physical thread. It defaults to false. |
| [HoleFeatureInput.setLengthAndOffset](HoleFeatureInput_setLengthAndOffset.htm) | Sets the length and offset of the thread of a tapped hole. |
| [HoleFeatureInput.setToClearanceHole](HoleFeatureInput_setToClearanceHole.htm) | Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object. |
| [HoleFeatureInput.setToSimpleHole](HoleFeatureInput_setToSimpleHole.htm) | This property sets the hole's tap to be "simple", which means that it will not have any tap and will be a simple hole. When a new input is created, it defaults to being a simple hole. |
| [HoleFeatureInput.setToTappedHole](HoleFeatureInput_setToTappedHole.htm) | Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object. |
| [HoleFeatureInput.threadLength](HoleFeatureInput_threadLength.htm) | Gets the thread length when the isFullLength property is False. Returns null when the isFullLength property is true. |
| [HoleFeatureInput.threadOffset](HoleFeatureInput_threadOffset.htm) | Gets the thread offset when the isFullLength property is False. Returns null when the isFullLength property is true. |
| [Joints.addInferredJoint](Joints_addInferredJoint.htm) | Creates a new inferred joint. |
| [Joints.createInferredJointInput](Joints_createInferredJointInput.htm) | Creates a joint input to define an inferred joint. Use functionality on the returned InferredJointInput to define the input needed to infer a joint. |
| [Machine.clearSimulationModel](Machine_clearSimulationModel.htm) | Clears the simulation model from the machine. |
| [MachineElements.addElement](MachineElements_addElement.htm) | Add a new machine element to the machine. |
| [MachineElements.createMachineElementInput](MachineElements_createMachineElementInput.htm) | Create a new MachineElementInput object for the specified type. This is intedned to be used to create/add new machine elements. |
| [MachineLibrary.doesPathExist](MachineLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [ModelParameter.textValue](ModelParameter_textValue.htm) | Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [ModelParameter.valueType](ModelParameter_valueType.htm) | Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |
| [OperationStrategy.is2DStrategy](OperationStrategy_is2DStrategy.htm) | Gets whether given OperationStrategy is a 2D strategy. |
| [OperationStrategy.is3DStrategy](OperationStrategy_is3DStrategy.htm) | Gets whether given OperationStrategy is a 3D strategy. |
| [OperationStrategy.isAdditiveStrategy](OperationStrategy_isAdditiveStrategy.htm) | Gets whether given OperationStrategy is an additive strategy. |
| [OperationStrategy.isCuttingStrategy](OperationStrategy_isCuttingStrategy.htm) | Gets whether given OperationStrategy is a cutting strategy. |
| [OperationStrategy.isDrillingStrategy](OperationStrategy_isDrillingStrategy.htm) | Gets whether given OperationStrategy is a drilling strategy. |
| [OperationStrategy.isFinishingStrategy](OperationStrategy_isFinishingStrategy.htm) | Gets whether given OperationStrategy is a finishing strategy. |
| [OperationStrategy.isMillingStrategy](OperationStrategy_isMillingStrategy.htm) | Gets whether given OperationStrategy is a milling strategy. |
| [OperationStrategy.isRotaryStrategy](OperationStrategy_isRotaryStrategy.htm) | Gets whether given OperationStrategy is a rotary strategy. |
| [OperationStrategy.isSupportStrategy](OperationStrategy_isSupportStrategy.htm) | Gets whether given OperationStrategy is an additive support strategy. |
| [OperationStrategy.isTurningStrategy](OperationStrategy_isTurningStrategy.htm) | Gets whether given OperationStrategy is a turning strategy. |
| [Parameter.textValue](Parameter_textValue.htm) | Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [Parameter.valueType](Parameter_valueType.htm) | Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |
| [PostLibrary.doesPathExist](PostLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [PrintSettingLibrary.doesPathExist](PrintSettingLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [StockMaterialLibrary.doesPathExist](StockMaterialLibrary_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [ThickenFeature.thickenType](ThickenFeature_thickenType.htm) | Gets and sets the thicken type for the thicken.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [ThickenFeatureInput.thickenType](ThickenFeatureInput_thickenType.htm) | The thicken type used when creating a thicken. The default value is SharpThickenType. |
| [ThreadDataQuery.create](ThreadDataQuery_create.htm) | Static method to create a new ThreadDataQuery object. The ThreadDataQuery object is a utility object that provides methods to query for the valid thread definitions defined in Fusion. This object provides similar functionality as the Thread and Hole command dialogs to find valid thread types, designations and classes which can be used to create thread and tapped hole features. |
| [ThreadDataQuery.isTapered](ThreadDataQuery_isTapered.htm) | Returns if this ThreadDataQuery was created to query for standard or tapered threads. |
| [ThreadFeature.hole](ThreadFeature_hole.htm) | If this thread feature is was created as the result of creating a tapped hole, this property will return the associated hole feature. If this is a standard thread feature, this property will return null. |
| [ThreadInfo.create](ThreadInfo_create.htm) | This method creates a new ThreadInfo object that can be used to create a thread or tapped-hole feature. The ThreadInfo object defines the type and size of the thread to create. When creating a thread, the type and size of the thread are defined by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information.   The thread type implicitly defines if the thread is standard or tapered. Tapered threads can only be used when creating tapped holes and are not supported for thread features. |
| [ThreadInfo.isRightHanded](ThreadInfo_isRightHanded.htm) | Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true. |
| [ThreadInfo.isTapered](ThreadInfo_isTapered.htm) | Indicates if this ThreadInfo object defines a standard or tapered thread. |
| [ThreadInfo.redefine](ThreadInfo_redefine.htm) | Method that redefines an existing ThreadInfo object. This is typically used to change the thread of an existing thread or tapped hole.   The ThreadInfo object defines the type and size of a thread by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information.   Tapered threads can only be used when creating or editing tapped holes and are not supported for thread features. |
| [ThreadInfo.taperAngle](ThreadInfo_taperAngle.htm) | Returns the angle of the tapered thread in centimeters.   This is only valid when isTapered is true. |
| [ThreadInfo.taperTapDrillDiameter](ThreadInfo_taperTapDrillDiameter.htm) | Returns the Diameter of the tap drill required to create this tap.   This is only valid when isTapered is true. |
| [ThreadInfo.taperThreadHeight](ThreadInfo_taperThreadHeight.htm) | Returns the height of a tapered thread in centimeters. This is only valid when isTapered is true. |
| [ThreadInfo.taperUsefulThreadLength](ThreadInfo_taperUsefulThreadLength.htm) | Returns the useful length of threads for a tapered thread in centimeters.   This is only valid when isTapered is true. |
| [ThreadInfo.taperWrenchMakeupInternalDiameter](ThreadInfo_taperWrenchMakeupInternalDiameter.htm) | The wrench makeup internal diameter for a taper pipe thread, also known as the effective thread diameter, is the diameter at the point where the thread engagement occurs when the pipe is tightened with a wrench.   This is only valid when isTapered is true. |
| [ToolLibraries.doesPathExist](ToolLibraries_doesPathExist.htm) | Checks if the given URL points to an existing folder or asset in the library. |
| [UserParameter.textValue](UserParameter_textValue.htm) | Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [UserParameter.valueType](UserParameter_valueType.htm) | Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |

Help created: Thursday, September 4, 2025 6:53 AM

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |