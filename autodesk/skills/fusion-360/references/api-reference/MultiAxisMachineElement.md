# MultiAxisMachineElement Object ![Preview](../images/TestTubeLarge.png)

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisMachineElement.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Machine element representing multi-axis machine settings.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MultiAxisMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFeedrateSettings](MultiAxisMachineElement_createFeedrateSettings.htm) | Creates a MultiAxisFeedrateSettings specialized object from the given input. |
| [createFeedrateSettingsInput](MultiAxisMachineElement_createFeedrateSettingsInput.htm) | Creates a MultiAxisFeedrateSettingsInput object to be used as input for creating MultiAxisFeedrateSettings objects. |
| [createRetractAndReconfigureSettings](MultiAxisMachineElement_createRetractAndReconfigureSettings.htm) | Creates a MultiAxisRetractAndReconfigureSettings object. Set this object on the retractAndReconfigureSettings property to apply the changes. |
| [createSingularitySettings](MultiAxisMachineElement_createSingularitySettings.htm) | Creates a MultiAxisSingularitySettings object. Set this object on the singularitySettings property to apply the changes. |
| [deleteMe](MultiAxisMachineElement_deleteMe.htm) | Delete this multi-axis machine element from the machine. |
| [staticTypeId](MultiAxisMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [elementId](MultiAxisMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [feedrateSettings](MultiAxisMachineElement_feedrateSettings.htm) | The multi-axis feedrate settings for this machine. For changes to to this object to take effect, re-assign them to this property. Cannot be set to null. |
| [isUsingVirtualTooltip](MultiAxisMachineElement_isUsingVirtualTooltip.htm) | Specifies if the position of the virtual tool tip (tool end) should be output. Only relevant for rotary head axes. |
| [isValid](MultiAxisMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MultiAxisMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [retractAndReconfigureSettings](MultiAxisMachineElement_retractAndReconfigureSettings.htm) | The multi-axis retract and reconfigure settings for this machine. For changes to to this object to take effect, re-assign them to this property. To not use multi-axis retract and reconfigure, set this to null. |
| [singularitySettings](MultiAxisMachineElement_singularitySettings.htm) | The multi-axis kinematics settings for this machine. For changes to to this object to take effect, re-assign them to this property. To not use multi-axis kinematics, set this to null. |
| [typeId](MultiAxisMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |