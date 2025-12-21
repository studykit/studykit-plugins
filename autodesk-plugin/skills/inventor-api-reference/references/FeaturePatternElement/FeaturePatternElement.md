# FeaturePatternElement Object

## Description

Represents a single instance within a feature pattern.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../FeaturePatternElement/FeaturePatternElement_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeaturePatternElement/FeaturePatternElement_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FeaturePatternElement/FeaturePatternElement_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Faces](../FeaturePatternElement/FeaturePatternElement_Faces.md) | Property that returns a collection object generated as a result of the feature. |
| [Index](../FeaturePatternElement/FeaturePatternElement_Index.md) | Property that returns the index of this element within the pattern. |
| [Parent](../FeaturePatternElement/FeaturePatternElement_Parent.md) | Property that returns the feature pattern this element is a member of. |
| [ResultFeatures](../FeaturePatternElement/FeaturePatternElement_ResultFeatures.md) | Property that returns the features that were created for this pattern element. These can be work planes, work axes, work points and work surfaces. |
| [Suppressed](../FeaturePatternElement/FeaturePatternElement_Suppressed.md) | Property that gets and sets whether the element is suppressed or not. A value of True indicates it is suppressed. |
| [Transform](../FeaturePatternElement/FeaturePatternElement_Transform.md) | Property that returns the transform that describes this occurrences relative position to the parent feature(s). The transform returned for the first element in a pattern (the parent feature(s)) will be an identity matrix. |
| [Type](../FeaturePatternElement/FeaturePatternElement_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FeaturePatternElementProxy.NativeObject](../FeaturePatternElementProxy/FeaturePatternElementProxy_NativeObject.md), [FeaturePatternElements.Item](../FeaturePatternElements/FeaturePatternElements_Item.md)

## Derived Classes

[FeaturePatternElementProxy](../FeaturePatternElementProxy/FeaturePatternElementProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |