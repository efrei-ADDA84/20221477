*TP4*


## Installation des outils

1. **Installation de Terraform et Azure CLI** :
   - Téléchargez et installez [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli) depuis le site officiel de Microsoft.
   - Téléchargez et installez [Terraform](https://www.terraform.io/downloads.html) depuis le site officiel de Terraform.

2. **Ajout des variables d'environnement** :
   - Après l'installation, ajoutez les chemins des exécutables de Azure CLI et Terraform à votre variable d'environnement `PATH` :
     ```
     C:\Program Files\Terraform
     C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin
     ```

## Déploiement des ressources avec Terraform

1. **Initialisation de Terraform** :
   Ouvrez une fenêtre de terminal et naviguez vers le répertoire contenant vos fichiers Terraform, puis exécutez la commande :

```
terraform init
```

![image](https://github.com/efrei-ADDA84/20221477/assets/129147663/4edcc7e2-22f0-4f42-afa2-9339ac7437f1)


2. **Planification des ressources Terraform** :
Une fois que Terraform est initialisé, planifiez les ressources à déployer avec la commande :
```
terraform plan
```
![image](https://github.com/efrei-ADDA84/20221477/assets/129147663/3eece3da-ab15-4f2a-b551-91bd3a85bef3)

3. **Déploiement des ressources Terraform** :
Après avoir vérifié le plan de déploiement, exécutez la commande pour déployer les ressources :
```
terraform apply
```
![image](https://github.com/efrei-ADDA84/20221477/assets/129147663/b33d4221-a8ec-4ff6-a532-ac97ba409949)


## Post-déploiement

1. **Récupération de l'adresse IP publique de la VM** :
- Accédez au portail Azure ou utilisez Azure CLI pour récupérer l'adresse IP publique de la machine virtuelle déployée.

2. **Génération de la clé privée SSH** :
- Générez une paire de clés SSH localement avec la commande :
  
  ```
  ssh-keygen -t rsa -b 4096 -C  "elyes.Salah@efrei.net"
  ```
  ![image](https://github.com/efrei-ADDA84/20221477/assets/129147663/ecb2dfb4-811a-437a-9029-4ea251d4342c)


3. **Récupération de la clé privée Terraform** :
- Si vous avez configuré Terraform pour générer une clé SSH, vous pouvez récupérer la clé privée avec la commande :
  ```
  terraform output private_key_pem > privatekey.pem
  ```

4. **Connexion SSH à la machine virtuelle** :
- Utilisez la clé privée générée pour vous connecter à la machine virtuelle avec la commande :
  
  ```
  ssh -i privatekey.pem devops@52.143.186.154
  ```

5. **Vérification du système d'exploitation de la VM** :
- Une fois connecté à la machine virtuelle, vérifiez le système d'exploitation avec la commande :
  
  ```
  ssh -i privatekey.pem devops@52.143.186.154 cat /etc/os-release
  ```
![image](https://github.com/efrei-ADDA84/20221477/assets/129147663/5ef1a0f6-9186-43bd-afdb-af11f5644506)

## Destruction des ressources Terraform

Une fois que vous avez terminé d'utiliser la machine virtuelle, assurez-vous de détruire les ressources pour éviter les coûts inutiles :
  ```
terraform destroy
  ```


En suivant ces étapes, vous pourrez déployer et gérer des ressources Azure à l'aide de Terraform sur votre machine Windows.


Difficulté : 
Pour la clé .pem il faut gérer la permission des droits sur le fichier car si trop d'autorisation, elle est considérée comme penetrable et pas valide 
