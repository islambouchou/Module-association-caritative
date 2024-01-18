# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class clientspec(models.Model):
#     _name = 'clientspec.clientspec'

#     name = fields.Char()

class CampagneDeDon(models.Model):
    _name = 'association.campagne'
    _description = "Les Campagne de dons"
    name = fields.Char(string="Nom_Compagne", required=True)
    d = fields.One2many(
        'association.don', 'campagne_id', string="Dons")
    #donns_ids = fields.One2many(
     #   'association.don', 'campagne_id', string="Dons")
 

class  Donateur(models.Model):
    _name = 'association.donateur'
    _description = "Les donateurs"

    name = fields.Char(string="Nom_donateur", required=True)
    #true
    don_ids = fields.One2many(
        'association.don', 'donateur_id', string="Dons")
 

class Don(models.Model):
    _name = 'association.don'
    _description = "Les dons"
    name = fields.Char(string="IdDon", required=True)

    date = fields.Date()
    #true
    objets_donne_ids = fields.One2many(
        "association.obj", "don_id", string="Objets donnes")
    #true
    beneficiaire_ids = fields.Many2many (
        "association.beneficiaire", string="Benificiares")
    #true
    donateur_id = fields.Many2one("association.donateur", 
        ondelete="cascade", string="donateur", required = True)
    #true
    campagne_id = fields.Many2one("association.campagne", 
        ondelete="cascade", string="compagne", required=True)


class Beneficiaire(models.Model):
    _name = 'association.beneficiaire'
    _description = "Les beneficiaires"
    name = fields.Char(string="Nom_beneficiaire", required=True)
    #true
    dons_ids = fields.Many2many (
        "association.don", string="Dons")
    

class Objets_donnes(models.Model):
    _name = 'association.obj'
    _description = "Objets_donnes"

    name = fields.Char(string="Nom_objet_donne", required=True)
    #true
    don_id = fields.Many2one("association.don",  
        ondelete="cascade", String = "don", required = True)



   