# ThreadFeatureProxy.ThreadedFace Property

Parent Object: [ThreadFeatureProxy](../ThreadFeatureProxy/ThreadFeatureProxy.md)

## Description

Property that returns the set of that the thread is applied to. Usually this is just the face that was input for application of the thread feature, but in the case where the original face has been cut by subsequent features, the multiple resulting faces will be returned.

## Syntax

ThreadFeatureProxy.**ThreadedFace**() As [Faces](../Faces/Faces.md)

## Property Value

This is a read only property whose value is a [Faces](../Faces/Faces.md).

## Version

Introduced in version 9
