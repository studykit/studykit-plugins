# UnwrapDefinition.Copy Method

Parent Object: [UnwrapDefinition](../UnwrapDefinition/UnwrapDefinition.md)

## Description

Method that creates a copy of this UnwrapDefinition object. The new UnwrapDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new unwrap feature.
One typical use of this method is when you need to make several changes to an existing unwrap feature. If you edit the UnwrapDefinition object associated with the unwrap feature, the feature will recompute after each edit. It’s more efficient to make a copy, edit the copy, and then assign the copy to the feature. This will result in a single recompute.
The UnwrapFeatures.CreateDefinition method can also be used to create an independent UnwrapDefinition object. The difference is that one created with the Copy method will have the same initial values as the object is was copied from. One that’s created with the CreateDefinition method will be initialized to predefined default values.

## Syntax

UnwrapDefinition.**Copy**() As [UnwrapDefinition](../UnwrapDefinition/UnwrapDefinition.md)

## Version

Introduced in version 2020
