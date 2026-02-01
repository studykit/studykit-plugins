# MachineToolStationInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineToolStationInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Object representing the set of inputs required to create a new MachineToolStation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineToolStationInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [coolants](MachineToolStationInput_coolants.htm) | The coolants that this tool station can use. See MachineToolStationCoolant for possible values. |
| [isValid](MachineToolStationInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxToolDiameter](MachineToolStationInput_maxToolDiameter.htm) | The maximum diameter in cm of the tool that can be held by this tool station. |
| [maxToolLength](MachineToolStationInput_maxToolLength.htm) | The maximum length in cm of the tool that can be held by this tool station. |
| [objectType](MachineToolStationInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [toolInterface](MachineToolStationInput_toolInterface.htm) | The type of interface that this tool station uses. (e.g. BT40, CAPTO C5, HSK A100, SK50, etc.) Note: All newline characters will be removed, and if the string contains only ASCII characters, it will be converted to uppercase. |

## Accessed From

[MachinePartInput.createToolStationInput](MachinePartInput_createToolStationInput.htm), [MachinePartInput.toolStationInput](MachinePartInput_toolStationInput.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |