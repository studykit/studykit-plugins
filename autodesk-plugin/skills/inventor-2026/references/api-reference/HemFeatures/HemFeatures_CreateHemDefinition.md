# HemFeatures.CreateHemDefinition Method

Parent Object: [HemFeatures](../HemFeatures/HemFeatures.md)

## Description

Method that creates a new HemDefinition object.

## Remarks

The object created does not represent a hem feature but instead is a representation of the information that defines a hem feature. You can use this object as input to the HemFeatures.Add method to create the actual hem feature. The HemDefinition object returned is fully defined and can be used to create a hem feature. However, defaults are used for most of the hem options so you may want to change some of the property values of the HemDefinition object before using it to create a hem feature.

## Syntax

HemFeatures.**CreateHemDefinition**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md) ) As [HemDefinition](../HemDefinition/HemDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection object that specifies the edges to create a hem feature on. |

## Version

Introduced in version 2010
