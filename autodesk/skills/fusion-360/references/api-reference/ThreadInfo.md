# ThreadInfo Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

This class defines the methods and properties that define the type and size of a thread. This object is used to create and query thread and tapped (straight and tapered) hole features. A new ThreadInfo object is created by using the ThreadInfo.create method. If the ThreadInfo object is obtained from an existing thread or hole feature, modifying the ThreadInfo object will modify the feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ThreadInfo_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](ThreadInfo_create.htm) | This method creates a new ThreadInfo object that can be used to create a thread or tapped-hole feature. The ThreadInfo object defines the type and size of the thread to create. When creating a thread, the type and size of the thread are defined by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information. |
| [redefine](ThreadInfo_redefine.htm) | Method that redefines an existing ThreadInfo object. This is typically used to change the thread of an existing thread or tapped hole.   The ThreadInfo object defines the type and size of a thread by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information.   Tapered threads can only be used when creating or editing tapped holes and are not supported for thread features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isInternal](ThreadInfo_isInternal.htm) | Returns and sets if the thread is an internal or external thread. A value of true indicates an internal thread. It defaults to true. |
| [isRightHanded](ThreadInfo_isRightHanded.htm) | Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true. |
| [isTapered](ThreadInfo_isTapered.htm) | Indicates if this ThreadInfo object defines a standard or tapered thread. |
| [isValid](ThreadInfo_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [majorDiameter](ThreadInfo_majorDiameter.htm) | Returns the value that defines the major diameter. The units are centimeters. |
| [minorDiameter](ThreadInfo_minorDiameter.htm) | Returns the value that defines the minor diameter. The units are centimeters. |
| [objectType](ThreadInfo_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [pitchDiameter](ThreadInfo_pitchDiameter.htm) | Returns the value that defines the pitch diameter. The units are centimeters. |
| [taperAngle](ThreadInfo_taperAngle.htm) | Returns the angle of the tapered thread in centimeters.   This is only valid when isTapered is true. |
| [taperTapDrillDiameter](ThreadInfo_taperTapDrillDiameter.htm) | Returns the Diameter of the tap drill required to create this tap.   This is only valid when isTapered is true. |
| [taperThreadHeight](ThreadInfo_taperThreadHeight.htm) | Returns the height of a tapered thread in centimeters. This is only valid when isTapered is true. |
| [taperUsefulThreadLength](ThreadInfo_taperUsefulThreadLength.htm) | Returns the useful length of threads for a tapered thread in centimeters.   This is only valid when isTapered is true. |
| [taperWrenchMakeupInternalDiameter](ThreadInfo_taperWrenchMakeupInternalDiameter.htm) | The wrench makeup internal diameter for a taper pipe thread, also known as the effective thread diameter, is the diameter at the point where the thread engagement occurs when the pipe is tightened with a wrench.   This is only valid when isTapered is true. |
| [threadAngle](ThreadInfo_threadAngle.htm) | Returns the value that defines the thread angle. The units are degrees. |
| [threadClass](ThreadInfo_threadClass.htm) | Returns and sets the string that defines the thread class. |
| [threadDesignation](ThreadInfo_threadDesignation.htm) | Returns and sets the string that defines the thread designation. |
| [threadPitch](ThreadInfo_threadPitch.htm) | Returns the value that defines the thread pitch. The units are centimeters. |
| [threadSize](ThreadInfo_threadSize.htm) | Returns the string that defines the thread size. |
| [threadType](ThreadInfo_threadType.htm) | Returns and sets the string that defines the thread type. |

## Accessed From

[HoleFeature.tappedHoleInfo](HoleFeature_tappedHoleInfo.htm), [ThreadFeature.threadInfo](ThreadFeature_threadInfo.htm), [ThreadFeatureInput.threadInfo](ThreadFeatureInput_threadInfo.htm), [ThreadFeatures.createThreadInfo](ThreadFeatures_createThreadInfo.htm), [ThreadInfo.create](ThreadInfo_create.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |