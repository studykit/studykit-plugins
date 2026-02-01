# Joints Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

The collection of joints in this component. This provides access to all existing joints and supports the ability to create new joints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Joints_add.htm) | Creates a new joint. |
| [addInferredJoint](Joints_addInferredJoint.htm) | ![Preview](../images/TestTubeSmall.png)Creates a new inferred joint. |
| [classType](Joints_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInferredJointInput](Joints_createInferredJointInput.htm) | ![Preview](../images/TestTubeSmall.png)Creates a joint input to define an inferred joint. Use functionality on the returned InferredJointInput to define the input needed to infer a joint. |
| [createInput](Joints_createInput.htm) | Creates a JointInput object, which is the API equivalent to the Joint command dialog. You you use methods and properties on the returned class to set the desired options, similar to providing input and setting options in the Joint command dialog. Once the settings are defined you call the Joints.add method passing in the JointInput object to create the actual joint. |
| [item](Joints_item.htm) | Function that returns the specified joint using an index into the collection. |
| [itemByName](Joints_itemByName.htm) | Function that returns the specified joint using a name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Joints_count.htm) | Returns number of joints in the collection. |
| [isValid](Joints_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Joints_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Component.joints](Component_joints.htm), [FlatPatternComponent.joints](FlatPatternComponent_joints.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BallJointMotion API Sample](BallJointMotionSample_Sample.htm) | Demonstrates creating a joint with ball joint motion |
| [CylindricalJointMotion API Sample](CylindricalJointMotionSample_Sample.htm) | Demonstrates creating a joint with cylindrical joint motion. |
| [Joint API Sample](JointSample_Sample.htm) | Demonstrates creating a new joint. |
| [Pin Slot Joint Motion API Sample](PinSlotJointMotionSample_Sample.htm) | Demonstrates creating a joint with pin slot joint motion |
| [Planar Joint Motion API Sample](PlanarJointMotionSample_Sample.htm) | Demonstrates creating a joint with planar joint motion |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |