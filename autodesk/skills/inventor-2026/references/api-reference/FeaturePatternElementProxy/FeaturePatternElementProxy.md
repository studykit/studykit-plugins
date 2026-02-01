# FeaturePatternElementProxy Object

Derived from: [FeaturePatternElement](../FeaturePatternElement/FeaturePatternElement.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../FeaturePatternElementProxy/FeaturePatternElementProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeaturePatternElementProxy/FeaturePatternElementProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FeaturePatternElementProxy/FeaturePatternElementProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../FeaturePatternElementProxy/FeaturePatternElementProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Faces](../FeaturePatternElementProxy/FeaturePatternElementProxy_Faces.md) | Property that returns a collection object generated as a result of the feature. |
| [Index](../FeaturePatternElementProxy/FeaturePatternElementProxy_Index.md) | Property that returns the index of this element within the pattern. |
| [NativeObject](../FeaturePatternElementProxy/FeaturePatternElementProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../FeaturePatternElementProxy/FeaturePatternElementProxy_Parent.md) | Property that returns the feature pattern this element is a member of. |
| [ResultFeatures](../FeaturePatternElementProxy/FeaturePatternElementProxy_ResultFeatures.md) | Property that returns the features that were created for this pattern element. These can be work planes, work axes, work points and work surfaces. |
| [Suppressed](../FeaturePatternElementProxy/FeaturePatternElementProxy_Suppressed.md) | Property that gets and sets whether the element is suppressed or not. A value of True indicates it is suppressed. |
| [Transform](../FeaturePatternElementProxy/FeaturePatternElementProxy_Transform.md) | Property that returns the transform that describes this occurrences relative position to the parent feature(s). The transform returned for the first element in a pattern (the parent feature(s)) will be an identity matrix. |
| [Type](../FeaturePatternElementProxy/FeaturePatternElementProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
