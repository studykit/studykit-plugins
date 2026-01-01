# ControllerConfigurationMachineElement Object

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ControllerConfigurationMachineElement.h>

## Description

Machine element representing controller settings for kinematics.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ControllerConfigurationMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [staticTypeId](ControllerConfigurationMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axisConfigurations](ControllerConfigurationMachineElement_axisConfigurations.htm) | Gets the collection of axis configuration objects. |
| [elementId](ControllerConfigurationMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [isValid](ControllerConfigurationMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxBlockProcessingSpeed](ControllerConfigurationMachineElement_maxBlockProcessingSpeed.htm) | Maximum block processing rate for the controller. |
| [maxNormalSpeed](ControllerConfigurationMachineElement_maxNormalSpeed.htm) | Global maximum non-rapid linear motion speed. Units are cm/s. |
| [nonTcpRapidInterpolationMode](ControllerConfigurationMachineElement_nonTcpRapidInterpolationMode.htm) | ![Preview](../images/TestTubeSmall.png)Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is inactive, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. |
| [objectType](ControllerConfigurationMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [tcpRapidInterpolationMode](ControllerConfigurationMachineElement_tcpRapidInterpolationMode.htm) | ![Preview](../images/TestTubeSmall.png)Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is active, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. Tool Tip adjusts the linear axes to keep the tool's tip positioned along the direct line between the start and finish points. |
| [typeId](ControllerConfigurationMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |