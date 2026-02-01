# UnwrapDefinition Object

## Description

UnwrapDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../UnwrapDefinition/UnwrapDefinition_Copy.md) | Method that creates a copy of this UnwrapDefinition object. The new UnwrapDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new unwrap feature. One typical use of this method is when you need to make several changes to an existing unwrap feature. If you edit the UnwrapDefinition object associated with the unwrap feature, the feature will recompute after each edit. It’s more efficient to make a copy, edit the copy, and then assign the copy to the feature. This will result in a single recompute.  The UnwrapFeatures.CreateDefinition method can also be used to create an independent UnwrapDefinition object. The difference is that one created with the Copy method will have the same initial values as the object is was copied from. One that’s created with the CreateDefinition method will be initialized to predefined default values. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UnwrapDefinition/UnwrapDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AutomaticFaceChain](../UnwrapDefinition/UnwrapDefinition_AutomaticFaceChain.md) | Read-write Property that gets and sets whether or not to use all tangentially connected faces. A value of True indicates that automatic face chaining of tangentially connected faces should be performed. |
| [InputFaces](../UnwrapDefinition/UnwrapDefinition_InputFaces.md) | Read-write property that gets and sets the faces to unwrap. |
| [LinearResult](../UnwrapDefinition/UnwrapDefinition_LinearResult.md) | Read-write property that gets and sets an EdgeCollection that specifies a set of consecutive edges to become a single colinear segment in the result. The edges should be from the faces in the Faces property and only outer edges that enclose the faces are valid. |
| [MergeResultBody](../UnwrapDefinition/UnwrapDefinition_MergeResultBody.md) | Read-write property that gets and sets whether merge the result body or not. |
| [Origin](../UnwrapDefinition/UnwrapDefinition_Origin.md) | Read-write property that gets and sets the vertex as origin. |
| [Parent](../UnwrapDefinition/UnwrapDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ResultAlignment](../UnwrapDefinition/UnwrapDefinition_ResultAlignment.md) | Read-write property that gets and sets alignment of the deformed result. |
| [RigidResult](../UnwrapDefinition/UnwrapDefinition_RigidResult.md) | Read-write property that gets and sets an EdgeCollection that specifies a set of consecutive planar edges to remain undeformed. |
| [SeamEdges](../UnwrapDefinition/UnwrapDefinition_SeamEdges.md) | Read-write property that gets and sets an EdgeCollection that specifies the seam edges. |
| [Type](../UnwrapDefinition/UnwrapDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[UnwrapDefinition.Copy](../UnwrapDefinition/UnwrapDefinition_Copy.md), [UnwrapFeature.Definition](../UnwrapFeature/UnwrapFeature_Definition.md), [UnwrapFeatureProxy.Definition](../UnwrapFeatureProxy/UnwrapFeatureProxy_Definition.md), [UnwrapFeatures.CreateDefinition](../UnwrapFeatures/UnwrapFeatures_CreateDefinition.md), [UnwrapFeatures.CreateDefinitionWithOptions](../UnwrapFeatures/UnwrapFeatures_CreateDefinitionWithOptions.md)

## Version

Introduced in version 2020
